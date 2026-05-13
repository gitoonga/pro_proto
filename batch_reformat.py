import sys
import os
import argparse
import uuid
import re
from striprtf.striprtf import rtf_to_text

# Add the buff_compiler directory to the path
sys.path.append(os.path.join(os.getcwd(), "ProPresenter7-Proto", "buff_compiler"))

try:
    import presentation_pb2
    import action_pb2
    import slide_pb2
    import graphicsData_pb2
    import basicTypes_pb2
    import cue_pb2
except ImportError as e:
    print(f"Error importing protobuf modules: {e}")
    sys.exit(1)


def create_uuid_msg():
    u = uuid.uuid4()
    msg = basicTypes_pb2.UUID()
    msg.string = str(u).upper()
    return msg


def get_plain_text(rtf_bytes):
    try:
        rtf_str = rtf_bytes.decode("utf-8", errors="ignore")
        text = rtf_to_text(rtf_str)
        # Clean up common RTF artifacts and whitespace
        text = text.replace("\r", "")
        # Remove extra empty lines and trim each line
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines)
    except Exception as e:
        print(f"  Error parsing RTF: {e}")
        return ""


def wrap_in_rtf(text, font_name="Arial-Black", font_size=80):
    # Standard template: White text, Center Aligned
    # fs is in half-points, so fs80 = 40pt
    rtf = (
        r"{\rtf1\ansi\ansicpg1252\deff0{\fonttbl{\f0\fnil\fcharset0 "
        + font_name
        + r";}}"
    )
    rtf += r"{\colortbl ;\red255\green255\blue255;}"
    rtf += r"\viewkind4\uc1\pard\cf1\f0\fs" + str(font_size) + r"\qc "
    # Replace newlines with \par
    rtf += text.replace("\n", r"\par ")
    rtf += r"\par}"
    return rtf.encode("utf-8")


def split_text_into_slides(text, max_lines=2):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    slides = []
    for i in range(0, len(lines), max_lines):
        slides.append("\n".join(lines[i : i + max_lines]))
    return slides


def process_presentation(input_path, output_path):
    print(f"Processing: {os.path.basename(input_path)}")
    presentation = presentation_pb2.Presentation()
    try:
        with open(input_path, "rb") as f:
            presentation.ParseFromString(f.read())
    except Exception as e:
        print(f"  Failed to read file: {e}")
        return

    # Map old Cue UUIDs to new Cue UUIDs (list because one cue might become many)
    uuid_mapping = {}

    new_cues = []
    for old_cue in presentation.cues:
        old_uuid = old_cue.uuid.string

        # 1. Extract text from this cue
        all_lines = []
        for action in old_cue.actions:
            if action.HasField("slide") and action.slide.HasField("presentation"):
                slide = action.slide.presentation.base_slide
                for element in slide.elements:
                    if element.element.HasField("text"):
                        txt = get_plain_text(element.element.text.rtf_data)
                        if txt:
                            all_lines.extend(txt.splitlines())

        # 2. Re-segment text
        slide_texts = split_text_into_slides("\n".join(all_lines), 2)

        # If no text was found, keep the cue as is (might be a background-only slide)
        if not slide_texts:
            new_cue = cue_pb2.Cue()
            new_cue.CopyFrom(old_cue)
            new_uuid = create_uuid_msg()
            new_cue.uuid.CopyFrom(new_uuid)
            new_cues.append(new_cue)
            uuid_mapping[old_uuid] = [new_uuid.string]
            continue

        # 3. Create new cues
        mapping_list = []
        for i, text in enumerate(slide_texts):
            new_cue = cue_pb2.Cue()
            new_cue.CopyFrom(old_cue)
            new_uuid = create_uuid_msg()
            new_cue.uuid.CopyFrom(new_uuid)
            mapping_list.append(new_uuid.string)

            if i > 0:
                new_cue.name = f"{old_cue.name} (part {i+1})"

            # Update the text
            found_text = False
            for action in new_cue.actions:
                if action.HasField("slide") and action.slide.HasField("presentation"):
                    slide = action.slide.presentation.base_slide
                    # Find the first text element and update it
                    for element in slide.elements:
                        if element.element.HasField("text"):
                            element.element.text.rtf_data = wrap_in_rtf(text)
                            found_text = True
                            break

            new_cues.append(new_cue)

        uuid_mapping[old_uuid] = mapping_list

    # 4. Update the presentation with new cues
    del presentation.cues[:]
    presentation.cues.extend(new_cues)

    # 5. Optional: Remove all existing backgrounds to ensure consistency
    # (In Pro7, backgrounds are usually Media Actions on cues)
    for cue in presentation.cues:
        # Filter out Media Actions (ActionType 2 or 12 or 13)
        # We'll just remove all actions that have 'media' field set
        remaining_actions = []
        for action in cue.actions:
            if not action.HasField("media"):
                remaining_actions.append(action)

        del cue.actions[:]
        cue.actions.extend(remaining_actions)

    # 6. Update cue_groups (Verse/Chorus headers)
    for cue_group in presentation.cue_groups:
        new_identifiers = []
        for old_id in cue_group.cue_identifiers:
            if old_id.string in uuid_mapping:
                for mapped_id in uuid_mapping[old_id.string]:
                    id_msg = basicTypes_pb2.UUID()
                    id_msg.string = mapped_id
                    new_identifiers.append(id_msg)
            else:
                new_identifiers.append(old_id)

        del cue_group.cue_identifiers[:]
        cue_group.cue_identifiers.extend(new_identifiers)

    # 6. Update arrangements
    for arrangement in presentation.arrangements:
        new_group_ids = []
        for old_group_id in arrangement.group_identifiers:
            # Arrangements point to Group UUIDs, not Cue UUIDs.
            # Since we didn't change Group UUIDs, this should still work.
            new_group_ids.append(old_group_id)
        # (Actually, we didn't touch Group UUIDs, so we don't need to update this unless we created new groups)

    # 7. Save
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(presentation.SerializeToString())
        print(f"  Saved to: {output_path}")
    except Exception as e:
        print(f"  Error saving: {e}")

def main():
    parser = argparse.ArgumentParser(description="Batch reformat ProPresenter 7 files.")
    parser.add_argument(
        "-i", "--input", 
        default=os.path.join(os.getcwd(), "test_files"),
        help="Directory containing .pro files to process (default: test_files/)"
    )
    parser.add_argument(
        "-o", "--output", 
        default=os.path.join(os.getcwd(), "output_files"),
        help="Directory to save reformatted files (default: output_files/)"
    )
    
    args = parser.parse_args()
    
    input_dir = args.input
    output_dir = args.output

    # SETTINGS
    # Set this to a path if you want a specific background applied to the first slide of every song
    # Example: r"C:\Users\Admin\Documents\ProPresenter\Media\Backgrounds\BlueMotion.mp4"
    standard_background_path = None

    # Formatting
    font_name = "Arial-Black"
    font_size = 80  # Half-points (40pt)

    if not os.path.exists(input_dir):
        print(f"Input directory not found: {input_dir}")
        return

    if not os.path.isdir(input_dir):
        print(f"Input path is not a directory: {input_dir}")
        return

    files = [f for f in os.listdir(input_dir) if f.endswith(".pro")]
    print(f"Found {len(files)} files in '{input_dir}' to process.")

    if not files:
        print("No .pro files found.")
        return

    for filename in files:
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        process_presentation(input_path, output_path)


if __name__ == "__main__":
    main()

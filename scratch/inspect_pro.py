import sys
import os

# Add the buff_compiler directory to the path so we can import the generated pb2 files
sys.path.append(os.path.join(os.getcwd(), 'ProPresenter7-Proto', 'buff_compiler'))

import presentation_pb2
import action_pb2
import slide_pb2
import graphicsData_pb2

def inspect_pro_file(file_path):
    print(f"Inspecting: {file_path}")
    presentation = presentation_pb2.Presentation()
    with open(file_path, 'rb') as f:
        presentation.ParseFromString(f.read())
    
    print(f"Presentation Name: {presentation.name}")
    print(f"Number of Cues: {len(presentation.cues)}")
    
    for i, cue in enumerate(presentation.cues):
        print(f"\nCue {i+1}: {cue.name}")
        for j, action in enumerate(cue.actions):
            if action.HasField('slide'):
                slide_type = action.slide
                if slide_type.HasField('presentation'):
                    presentation_slide = slide_type.presentation
                    base_slide = presentation_slide.base_slide
                    for k, element in enumerate(base_slide.elements):
                        graphics_element = element.element
                        if graphics_element.HasField('text'):
                            text_obj = graphics_element.text
                            # rtf_data is bytes
                            rtf_text = text_obj.rtf_data.decode('utf-8', errors='ignore')
                            print(f"  Action {j+1}, Element {k+1} (Text):")
                            # Just print first 100 chars of RTF to avoid flooding
                            print(f"    RTF Snippet: {rtf_text[:100]}...")

if __name__ == "__main__":
    test_file = r"d:\python\pro_proto\output_files\A Heart Like Thine.pro"
    if os.path.exists(test_file):
        inspect_pro_file(test_file)
    else:
        print("Test file not found.")

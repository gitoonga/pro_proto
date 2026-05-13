# ProPresenter 7 Batch Reformatter

A Python-based automation tool designed to standardize and reformat ProPresenter 7 song files (`.pro`) at scale. This tool is particularly useful for cleaning up large libraries (1000+ songs) to ensure consistent typography, slide length, and layout.

## 🚀 Key Features

- **Automatic Slide Re-segmentation**: Automatically splits song lyrics into slides with a maximum of **2 lines per slide**, ensuring optimal readability.
- **Consistent Typography**: Applies a standardized RTF-based format (White text, Center Aligned, Arial Black, 40pt) to all slides.
- **Bulk Processing**: Processes all `.pro` files in an input directory and outputs them to a designated folder.
- **Structure Preservation**: Maintains original song components including **Groups** (Verse, Chorus, Bridge, etc.) and **Arrangements**.
- **Background Cleanup**: Strips existing media actions/backgrounds from slides to provide a clean slate for new visual themes.
- **Protobuf Driven**: Uses ProPresenter 7's native Protocol Buffer format for high-fidelity file manipulation.

## 🛠️ Prerequisites

- **Python 3.8 or higher**
- `pip` (Python package installer)

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gitoonga/pro_proto.git
   cd pro_proto
   ```

2. **Setup the Virtual Environment**:
   - **Windows (PowerShell)**:
     ```powershell
     .\setup_venv.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     setup_venv.bat
     ```

3. **Activate the environment**:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

## 📖 Usage

### Basic Usage (using default folders)
1. **Prepare Input Files**: Place the `.pro` files you want to reformat into the `test_files/` directory.
2. **Run the Script**:
   ```bash
   python batch_reformat.py
   ```
3. **Retrieve Results**: The reformatted files will be generated in the `output_files/` directory.

### Advanced Usage (custom paths)
You can specify custom input and output directories using command-line arguments:
```bash
python batch_reformat.py --input "C:\Path\To\My\Songs" --output "C:\Path\To\Output"
```
Or using short flags:
```bash
python batch_reformat.py -i "C:\Path\To\My\Songs" -o "C:\Path\To\Output"
```

## ⚙️ Customization

You can easily customize the formatting by editing the `SETTINGS` block in `batch_reformat.py`:

```python
# batch_reformat.py

# Formatting Settings
font_name = "Arial-Black"
font_size = 80  # Half-points (e.g., 80 = 40pt)
max_lines = 2   # Maximum lines per slide
```

## 📂 Project Structure

- `batch_reformat.py`: The main automation script.
- `ProPresenter7-Proto/`: Contains the protobuf definitions and generated Python classes.
- `test_files/`: Input directory for original `.pro` files.
- `output_files/`: Output directory for processed files.
- `requirements.txt`: Python dependencies (`protobuf`, `striprtf`).

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
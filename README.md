**ProPresenter Proto Compiler and Decoder**
==========================================

This repository contains two Python scripts that automate the compilation and decoding of Proto files for ProPresenter.

**Compilation Script**
---------------------

The first script compiles `.proto` files in the `proto` folder and generates Python output in the `buff_compiler` folder.

**Usage**

1. Place your `.proto` files in the `proto` folder.
2. Run the script to compile the files.
3. The compiled Python files will be generated in the `buff_compiler` folder.

**Decoding Script**
-----------------

The second script decodes `.pro` files in the `test_files` folder and generates text output in the `txt_output` folder.

**Usage**

1. Place your `.pro` files in the `test_files` folder.
2. Run the script to decode the files.
3. The decoded text files will be generated in the `txt_output` folder.

**Requirements**
---------------

* Python 3.x
* `protoc` compiler installed on your system

**Running the Scripts**
---------------------

1. Open a terminal or command prompt.
2. Navigate to the repository folder.
3. Run the script using `python script_name.py` (replace `script_name.py` with the name of the script you want to run).

**Troubleshooting**
-----------------

If you encounter any issues, check the script output for error messages. Make sure you have the `protoc` compiler installed and configured correctly.

**License**
-------

This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT).
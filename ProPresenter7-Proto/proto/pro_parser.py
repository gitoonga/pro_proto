import os
import subprocess
import time

print("Starting ...")

folder = r"D:\Unc\proto\test_files"
output_folder = r"D:\Unc\proto\test_files\txt_output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder):
    start_time = time.time()
    
    input_file = os.path.join(folder, filename)
    output_file = os.path.join(output_folder, f"{filename}.txt")
    
    protoc_command = ["protoc", "--decode", "rv.data.Presentation", "./propresenter.proto", "<", input_file, ">", output_file]
    
    print(f"Processing: {input_file}", end="")
    
    if filename.endswith('pro'):
        run = subprocess.run(protoc_command, capture_output=True)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"...{elapsed_time:.2f} seconds",end="")
        
        if run.returncode == 0:
            print(" Success")
        else:
            print(f"Error: {run.stderr}")
            
print("Done")
import os
import subprocess
import time

print("Starting ...")

folder = r"D:\Unc\proto\ProPresenter7-Proto\proto"
output_folder = r"D:\Unc\proto\ProPresenter7-Proto\buff_compiler"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder):
    start_time = time.time()
    protoc_command = ["protoc", f"-I={folder}", f"--python_out={output_folder}", filename]
    
    print(f"Processing: {os.path.join(folder, filename)}", end="")
    
    if filename.endswith('proto'):
        run = subprocess.run(protoc_command, capture_output=True)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"...{elapsed_time:.2f} seconds",end="")
        
        if run.returncode == 0:
            print(" Success")
        else:
            print(f"Error: {run.stderr}")
            
print("Done")
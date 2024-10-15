import os
import filecmp
import shutil

def copy_if_different(folder1, folder2):
    for dirpath, _, filenames in os.walk(folder1):
        # Construct the relative path from folder1
        relative_dir = os.path.relpath(dirpath, folder1)
        folder2_dirpath = os.path.join(folder2, relative_dir)
        
        # Ensure corresponding directory exists in folder2
        if not os.path.exists(folder2_dirpath):
            print(f"{folder2_dirpath} doesn't exist")
        
        for filename in filenames:
            file1_path = os.path.join(dirpath, filename)
            file2_path = os.path.join(folder2_dirpath, filename)
            
            # Copy the file if it doesn't exist in folder2 or is different
            if not os.path.exists(file2_path) or not filecmp.cmp(file1_path, file2_path, shallow=False):
                shutil.copy2(file1_path, file2_path)
                print(f"Copied: {file1_path} to {file2_path}")

# copy changed files from own repo to existing cm repo:
folder1 = '.'
folder2 = '../mlcommons@cm4mlops'
copy_if_different(folder1, folder2)

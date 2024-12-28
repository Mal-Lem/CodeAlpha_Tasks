import os
import shutil

def organize_files(directory):
    # ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # skip directories
        if os.path.isdir(file_path):
            continue
        
        # extract the file extension
        _, file_extension = os.path.splitext(filename)
        if file_extension:
            # remove the dot from the extension
            file_extension = file_extension[1:]
            
            # create a folder for the file extension if it doesn't exist
            target_folder = os.path.join(directory, file_extension.upper())
            os.makedirs(target_folder, exist_ok=True)
            
            # move the file to the appropriate folder
            shutil.move(file_path, os.path.join(target_folder, filename))
    
    print(f"Files in '{directory}' have been organized by extension.")

# provide the directory path
directory_path = input("Enter the directory to organize: ")
organize_files(directory_path)

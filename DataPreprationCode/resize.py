import os
from PIL import Image
from shutil import copy2

# Set the target size for resizing
TARGET_WIDTH = 640
TARGET_HEIGHT = 480

# Define the main directory where the subfolders are located
# main_directory = r'C:\Users\Developer\MyProjects\DME\Groundtruth\testFoldder\Inputdata\Selected_folders'  # Replace with the actual path
main_directory = r'C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\Dataset\All_Data'  # Replace with the actual path
icount = 1
# Function to process images
def process_images(icount = icount):
    for root, dirs, files in os.walk(main_directory):
        for dir_name in dirs:
            if dir_name == 'Red_OutputFinal':
                parent_folder_name = os.path.basename(root)
                _OutputFinal_path = os.path.join(root, dir_name)
                _OutputFinal_resize_path = os.path.join(root, dir_name+'_resize')
                
                # Print the name of the parent folder containing "_OutputFinal"
                print(f"icount = {icount}, Processing parent folder: {parent_folder_name}")
                icount = icount + 1
                # Create the new folder if it doesn't exist
                os.makedirs(_OutputFinal_resize_path, exist_ok=True)
                
                for file_name in os.listdir(_OutputFinal_path):
                    file_path = os.path.join(_OutputFinal_path, file_name)
                    
                    # Check if the file is an image
                    if file_name.lower().endswith(('.png')):
                        with Image.open(file_path) as img:
                            # Get the current size of the image
                            width, height = img.size
                            
                            # Check if resizing is necessary
                            if width != TARGET_WIDTH or height != TARGET_HEIGHT:
                                # Resize the image using the LANCZOS filter
                                img_resized = img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)
                                img_resized.save(os.path.join(_OutputFinal_resize_path, file_name))
                            else:
                                # If resizing is not necessary, just copy the file
                                copy2(file_path, _OutputFinal_resize_path)

# Call the function to process the images
process_images(icount)

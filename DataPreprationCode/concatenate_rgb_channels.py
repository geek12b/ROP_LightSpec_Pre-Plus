import os
from PIL import Image
import numpy as np

# Define the directories for the Red, Green, and Blue channels
# FolderDir = "stage3"
base_dir = r"C:\Users\Developer\MyProjects\DR_Fundus_Study\Dataset\RawImages"
# base_dir = os.path.join(base_dir, FolderDir)

red_dir = os.path.join(base_dir, "Red_OutputFinal")
green_dir = os.path.join(base_dir, "Green_OutputFinal")
blue_dir = os.path.join(base_dir, "Blue_OutputFinal")

imageFormat = '.tif'
# Directory to save the final RGB images
output_dir = os.path.join(base_dir, "RGB_OutputFinal")
os.makedirs(output_dir, exist_ok=True)

# Function to concatenate the RGB channels and save the image
def concatenate_channels_and_save(red_img, green_img, blue_img, output_path):
    # Open the images
    red = Image.open(red_img)
    green = Image.open(green_img)
    blue = Image.open(blue_img)
    
    # Ensure all channels are the same size
    red = red.resize(green.size) if red.size != green.size else red
    blue = blue.resize(green.size) if blue.size != green.size else blue
    
    # Merge into RGB format
    rgb_image = Image.merge("RGB", (red, green, blue))
    
    # Save the final image
    rgb_image.save(output_path)

# Loop through the red directory and find corresponding green and blue images
for ith , red_image_filename in enumerate(os.listdir(red_dir), start = 1):
    if red_image_filename.endswith(imageFormat):
        # Construct full file paths
        red_image_path = os.path.join(red_dir, red_image_filename)
        
        # Find corresponding green and blue images
        green_image_path = os.path.join(green_dir, red_image_filename)
        blue_image_path = os.path.join(blue_dir, red_image_filename)
        
        if os.path.exists(green_image_path) and os.path.exists(blue_image_path):
            # Create the output path
            output_image_path = os.path.join(output_dir, red_image_filename)
            
            # Concatenate and save the channels
            concatenate_channels_and_save(red_image_path, green_image_path, blue_image_path, output_image_path)
        else:
            print(f"Missing green or blue channel for {red_image_filename}")
        
        print(f"ith: {ith} {red_image_filename}")
            
print(f"RGB images saved to: {output_dir}")

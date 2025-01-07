import os
import cv2
import numpy as np

# Define paths
input_dir = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\Dataset\All_Data\RGB_OutputFinal"
# output_dir_masks = r"C:\Users\Developer\MyProjects\ARVO2025\Masks"
output_dir_masks = os.path.join(input_dir, "Masks")
output_dir_red_channel = os.path.join(input_dir, "RedChannel")
# output_dir_red_channel = r"C:\Users\Developer\MyProjects\ARVO2025\RedChannel"

# Create output directories if they don't exist
os.makedirs(output_dir_masks, exist_ok=True)
os.makedirs(output_dir_red_channel, exist_ok=True)

# Iterate through all .tif images in the input directory
for ith, filename in enumerate(os.listdir(input_dir), start = 1):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        file_path = os.path.join(input_dir, filename)
        
        # Read the image
        image = cv2.imread(file_path)
        
        # Extract the red channel
        red_channel = image[:, :, 2]
        
        # Create a mask where red channel values are greater than 0
        _, mask = cv2.threshold(red_channel, 5, 255, cv2.THRESH_BINARY)
        
        # Save the mask with the same name in the masks output directory
        mask_output_path = os.path.join(output_dir_masks, filename)
        cv2.imwrite(mask_output_path, mask)
        
        # Save the red channel with the same name in the red channel output directory
        red_channel_output_path = os.path.join(output_dir_red_channel, filename)
        cv2.imwrite(red_channel_output_path, red_channel)
        print(f"ith: {ith}  {filename}")

print(f"Masks have been saved in {output_dir_masks}.")
print(f"Red channels have been saved in {output_dir_red_channel}.")

import os
import cv2
import numpy as np

# Define the input and output directories
input_dir = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\Dataset\All_Data\RGB_OutputFinal"
output_dir = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\Dataset\All_Data\RGG_Output"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process all images in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # Check for image files
        # Read the RGB image
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)

        if img is not None:
            # Split channels (OpenCV loads images in BGR format)
            B, G, R = cv2.split(img)

            # Create new image with RGG format (duplicate green channel, remove blue)
            RGG_image = cv2.merge([R, G, G])  # (Red, Green, Green)

            # Save the modified image
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, RGG_image)

            # Print status update
            print(f"Processed: {filename} -> Saved as RGG format")

print(f"All images processed and saved in: {output_dir}")

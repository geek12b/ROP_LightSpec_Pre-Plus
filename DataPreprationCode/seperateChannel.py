import os
import cv2
import numpy as np

def resize_and_split_channels(input_directory):
    # Ensure output directories for each channel exist
    output_dirs = {
        'red': os.path.join(input_directory, 'Red_OutputFinal'),
        'green': os.path.join(input_directory, 'Green_OutputFinal'),
        'blue': os.path.join(input_directory, 'Blue_OutputFinal')
    }

    for key, path in output_dirs.items():
        os.makedirs(path, exist_ok=True)

    # Resize dimensions
    width, height = 640, 480

    # Loop through files in the input directory
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)

        if os.path.isfile(file_path):
            # Read the image
            image = cv2.imread(file_path)

            if image is not None:
                # Resize the image
                resized_image = cv2.resize(image, (width, height))

                # Split into channels
                blue_channel, green_channel, red_channel = cv2.split(resized_image)

                # Save each channel with the same file format
                base_name, ext = os.path.splitext(filename)

                cv2.imwrite(
                    os.path.join(output_dirs['red'], f"{base_name}{ext}"),
                    red_channel
                )
                cv2.imwrite(
                    os.path.join(output_dirs['green'], f"{base_name}{ext}"),
                    green_channel
                )
                cv2.imwrite(
                    os.path.join(output_dirs['blue'], f"{base_name}{ext}"),
                    blue_channel
                )

if __name__ == "__main__":
    input_dir = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\Dataset\All_Data\RGB_OutputFinal"
    resize_and_split_channels(input_dir)

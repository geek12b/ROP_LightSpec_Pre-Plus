import os
import cv2
import numpy as np

# === CONFIGURABLE PARAMETERS ===
CROP_SIZE = 256  # Change this to any value like 224, 256, etc.
INPUT_DIR = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\Dataset\All_Data\DR_RGB_OutputFinal_test"
# ================================

# Output folders
output_cropped_dir = os.path.join(INPUT_DIR, f"Cropped_{CROP_SIZE}")
output_r_dir = os.path.join(INPUT_DIR, f"Cropped_R_{CROP_SIZE}")
output_g_dir = os.path.join(INPUT_DIR, f"Cropped_G_{CROP_SIZE}")
output_b_dir = os.path.join(INPUT_DIR, f"Cropped_B_{CROP_SIZE}")

# Create output directories
os.makedirs(output_cropped_dir, exist_ok=True)
os.makedirs(output_r_dir, exist_ok=True)
os.makedirs(output_g_dir, exist_ok=True)
os.makedirs(output_b_dir, exist_ok=True)

# Loop through all files in input directory
for filename in os.listdir(INPUT_DIR):
    file_path = os.path.join(INPUT_DIR, filename)
    if not os.path.isfile(file_path):
        continue

    # Read the image
    img = cv2.imread(file_path)
    if img is None:
        print(f"Skipping {filename}: not a valid image.")
        continue

    h, w, _ = img.shape
    if h < CROP_SIZE or w < CROP_SIZE:
        print(f"Skipping {filename}: image smaller than crop size {CROP_SIZE}.")
        continue

    # Calculate center crop coordinates
    center_y, center_x = h // 2, w // 2
    half_crop = CROP_SIZE // 2
    cropped_img = img[center_y - half_crop:center_y + half_crop,
                      center_x - half_crop:center_x + half_crop]

    # Save cropped image
    cropped_path = os.path.join(output_cropped_dir, filename)
    cv2.imwrite(cropped_path, cropped_img)

    # Split RGB and save each channel
    b, g, r = cv2.split(cropped_img)
    cv2.imwrite(os.path.join(output_r_dir, filename), r)
    cv2.imwrite(os.path.join(output_g_dir, filename), g)
    cv2.imwrite(os.path.join(output_b_dir, filename), b)

print(f"Processing complete for {CROP_SIZE}x{CROP_SIZE} crops.")

import pandas as pd
import os
import re
import shutil
import glob

# Define file paths
input_csv = r"C:\\Users\\Developer\\MyProjects\\ROP_Pre-Plus_LightSpec\\xlsx_generated\\unique_posterior_eye_3_Accept_Image.csv"
source_directory = r"F:\\iROP\\fundus\\fundus"
destination_directory = r"F:\\ROP_Pre-Plus_LightSpec\\Archive_01-03-25"
output_csv = r"C:\\Users\\Developer\\MyProjects\\ROP_Pre-Plus_LightSpec\\xlsx_generated\\unique_posterior_eye_3_Accept_Image_Exist_Images.csv"

# Ensure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Read the CSV file
data = pd.read_csv(input_csv)

# Filter rows where 'Golden Reading Image Set Quality' is 'Acceptable for diagnosis'
# and 'Golden Reading Plus' is not 'Unknown' (case-insensitive)
filtered_data = data[
    (data['Golden Reading Image Set Quality'].str.lower() == 'acceptable for diagnosis') &
    (data['Golden Reading Plus'].str.lower() != 'unknown')
]

# Extract unique identifiers from the 'posterior' column
filtered_data['image_id'] = filtered_data['posterior'].apply(
    lambda x: ((re.search(r"(\d+)_", str(x)).group(1)) + ".png") if pd.notna(x) and re.search(r"(\d+)_", str(x)) else None
)

# Drop rows with no valid image_id
filtered_data = filtered_data.dropna(subset=['image_id'])

# Keep track of rows with existing images
existing_images_data = []

# Iterate through each extracted image_id and find files with any extension
for _, row in filtered_data.iterrows():
    image_id = row['image_id']
    # Generalized search pattern for files with any extension
    search_pattern = os.path.join(source_directory, f"{image_id}")
    matching_files = glob.glob(search_pattern)

    if matching_files:
        for file in matching_files:
            destination_file = os.path.join(destination_directory, os.path.basename(file))
            shutil.copy2(file, destination_file)
            print(f"Copied: {file} to {destination_file}")
        # Add the row to the list of existing images
        existing_images_data.append(row)
    else:
        print(f"No matching files found for: {image_id}")

# Create a DataFrame for rows with existing images
existing_images_df = pd.DataFrame(existing_images_data)

# Save the updated DataFrame to a new CSV file
existing_images_df.to_csv(output_csv, index=False)

print("Image extraction and copying completed for 'Acceptable for diagnosis' and 'Golden Reading Plus' not 'Unknown' (case-insensitive).")
print(f"New CSV with existing images saved to: {output_csv}")

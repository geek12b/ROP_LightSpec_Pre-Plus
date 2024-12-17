import os
import pandas as pd

# Define paths
base_dir = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec"
source_file = os.path.join(base_dir, "SusanData_2023-0320.xlsx")
output_file = os.path.join(base_dir, "Filtered_SusanData_2023-0320.xlsx")

# Load the Excel file
data = pd.read_excel(source_file)

# Define the columns to check for content
columns_to_check = ["posterior", "temporal", "nasal", "superior", "inferior"]

# Filter rows where at least one of the specified columns has content
filtered_data = data.dropna(subset=columns_to_check, how='all')

# Save the filtered data to a new file
filtered_data.to_excel(output_file, index=False)
# print(f"Filtered data saved to {output_file}")

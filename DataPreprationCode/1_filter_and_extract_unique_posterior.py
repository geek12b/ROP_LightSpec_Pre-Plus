import pandas as pd
import os
import re

# Define file paths
directory = "C:\\Users\\Developer\\MyProjects\\ROP_Pre-Plus_LightSpec"
input_file = os.path.join(directory, "SusanData_2023-0320.xlsx")
output_file_filtered = os.path.join(directory, "filtered_posterior.csv")
output_file_unique = os.path.join(directory, "unique_posterior.csv")

# Read the Excel file
data = pd.read_excel(input_file)

# Filter rows where the 'posterior' column is not null or empty
filtered_data = data[data['posterior'].notna() & data['posterior'].astype(str).str.strip().ne("")]

# Save the filtered data to a CSV file
filtered_data.to_csv(output_file_filtered, index=False)

# Extract unique identifiers (e.g., '41133_') from 'posterior' column
filtered_data['posterior_id'] = filtered_data['posterior'].apply(
    lambda x: re.search(r"(\d+_)", str(x)).group(1) if pd.notna(x) and re.search(r"(\d+_)", str(x)) else None
)

# Drop duplicates based on the extracted 'posterior_id' while keeping the whole row
unique_data = filtered_data.drop_duplicates(subset=['posterior_id'])

# Drop the temporary 'posterior_id' column
unique_data = unique_data.drop(columns=['posterior_id'])

# Save the unique data to another CSV file
unique_data.to_csv(output_file_unique, index=False)

print(f"Filtered data saved to: {output_file_filtered}")
print(f"Unique data saved to: {output_file_unique}")

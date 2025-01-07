import pandas as pd
import os
import re

# Define file paths
directory = "C:\\Users\\Developer\\MyProjects\\ROP_Pre-Plus_LightSpec\\xlsx_generated"
input_file = os.path.join(directory, "SusanData_2023-0320.xlsx")
output_file_filtered = os.path.join(directory, "filtered_posterior_with_id.csv")
output_file_unique = os.path.join(directory, "unique_posterior_with_id.csv")

# Read the Excel file
data = pd.read_excel(input_file)

# Modify "Golden Reading Plus" column
data["Golden Reading Plus"] = data["Golden Reading Plus"].replace({
    "No": "A_No",
    "Pre-Plus": "B_Pre-Plus",
    "Plus": "C_Plus"
})

# Filter rows where the 'posterior' column is not null or empty
filtered_data = data[data['posterior'].notna() & data['posterior'].astype(str).str.strip().ne("")]

# Extract unique identifiers (e.g., '41133') from 'posterior' column, add '.png', and save in a new column 'posterior_id'
filtered_data['posterior_id'] = filtered_data['posterior'].apply(
    lambda x: ((re.search(r"(\d+)_", str(x)).group(1)) + ".png") if pd.notna(x) and re.search(r"(\d+)_", str(x)) else None
)

# Save the filtered data with the 'posterior_id' column to a CSV file
filtered_data.to_csv(output_file_filtered, index=False)

# Drop duplicates based on the 'posterior_id' while keeping the whole row
unique_data = filtered_data.drop_duplicates(subset=['posterior_id'])

# Save the unique data with the 'posterior_id' column to another CSV file
unique_data.to_csv(output_file_unique, index=False)

print(f"Filtered data with 'posterior_id' saved to: {output_file_filtered}")
print(f"Unique data with 'posterior_id' saved to: {output_file_unique}")

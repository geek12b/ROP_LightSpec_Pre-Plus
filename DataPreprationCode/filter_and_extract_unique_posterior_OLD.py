import pandas as pd
import os

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

# Get rows with unique values in the 'posterior' column
unique_data = filtered_data.drop_duplicates(subset=['posterior'])

# Save the unique data to another CSV file
unique_data.to_csv(output_file_unique, index=False)

print(f"Filtered data saved to: {output_file_filtered}")
print(f"Unique data saved to: {output_file_unique}")

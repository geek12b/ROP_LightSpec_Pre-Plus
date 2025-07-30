import pandas as pd
import os

# Define file path
directory = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\xlsx_generated"
# input_file = os.path.join(directory, "unique_posterior_with_id.csv")
input_file = os.path.join(directory, "unique_posterior_eye_3_Accept_Image_Exist_Images.csv")

# Read the CSV file
data = pd.read_csv(input_file)

# Count occurrences of each value in the 'Golden Reading Plus' column
plus_counts = data['Golden Reading Plus'].value_counts()

# Print the counts for 'Golden Reading Plus'
print("Counts for 'Golden Reading Plus':")
print(plus_counts)

# Count occurrences of each value in the 'Golden Reading Image Set Quality' column
quality_counts = data['Golden Reading Image Set Quality'].value_counts()

# Print the counts for 'Golden Reading Image Set Quality'
print("Counts for 'Golden Reading Image Set Quality':")
print(quality_counts)


# Count occurrences of each value in the 'Golden Reading Image Set Quality' column
subjectID_data = data[data['subjectID'].notna() & data['subjectID'].astype(str).str.strip().ne("")]
Subjects_counts = subjectID_data['subjectID'].drop_duplicates()

# Print the counts for 'Golden Reading Image Set Quality'
print("#############Subjects_counts':")
print(Subjects_counts.count())

# Filter rows where 'Golden Reading Image Set Quality' is 'Acceptable for diagnosis'
acceptable_data = data[data['Golden Reading Image Set Quality'] == 'Acceptable for diagnosis']

# Count occurrences of each value in 'Golden Reading Plus' for 'Acceptable for diagnosis'
acceptable_plus_counts = acceptable_data['Golden Reading Plus'].value_counts()

# Print the counts for 'Golden Reading Plus' within 'Acceptable for diagnosis'
print("Counts for 'Golden Reading Plus' within 'Acceptable for diagnosis':")
print(acceptable_plus_counts)

# Save counts to a CSV file (optional)
output_file_plus = os.path.join(directory, "golden_reading_plus_counts.csv")
plus_counts.to_csv(output_file_plus, header=['Count'])

output_file_quality = os.path.join(directory, "golden_reading_quality_counts.csv")
quality_counts.to_csv(output_file_quality, header=['Count'])

output_file_acceptable_plus = os.path.join(directory, "acceptable_golden_reading_plus_counts.csv")
acceptable_plus_counts.to_csv(output_file_acceptable_plus, header=['Count'])

print(f"Counts for 'Golden Reading Plus' saved to: {output_file_plus}")
print(f"Counts for 'Golden Reading Image Set Quality' saved to: {output_file_quality}")
print(f"Counts for 'Golden Reading Plus' within 'Acceptable for diagnosis' saved to: {output_file_acceptable_plus}")

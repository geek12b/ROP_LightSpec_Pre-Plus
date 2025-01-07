import pandas as pd

# Define file paths
input_file = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\xlsx_generated\unique_posterior_with_id.csv"
output_file = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\xlsx_generated\unique_posterior_eye_2_.csv"
output_file_3 = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\xlsx_generated\unique_posterior_eye_3_AcceptPossib_Image.csv"
output_file_4 = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\xlsx_generated\unique_posterior_eye_3_Accept_Image.csv"

# Read the CSV file
data = pd.read_csv(input_file)

# Check required columns are present
if 'subjectID' in data.columns and 'eye' in data.columns:
    # Count total entries in 'subjectID'
    total_subjects = data['subjectID'].nunique()
    total_entries = len(data['subjectID'])
    print(f"Total entries in 'subjectID': {total_entries}")
    print(f"Unique 'subjectID' count: {total_subjects}")

    # Filter for each 'subjectID' to keep exactly one 'od' and one 'os', keeping the first entries
    def filter_first_od_os(group):
        return group[group['eye'].isin(['od', 'os'])].drop_duplicates(subset='eye', keep='first')

    filtered_data = data.groupby('subjectID', group_keys=False).apply(filter_first_od_os)

    # Save the filtered data to a new CSV file
    filtered_data.to_csv(output_file, index=False)
    print(f"Filtered data saved to {output_file}")


    # Additional filtering based on quality and plus criteria on filtered_data
    filtered_quality_data = filtered_data[((filtered_data['Golden Reading Image Set Quality'].str.lower() == 'acceptable for diagnosis') |
                                          (filtered_data['Golden Reading Image Set Quality'].str.lower() == 'possibly acceptable for diagnosis')) &
                                          (filtered_data['Golden Reading Plus'].str.lower() != 'unknown')]

    # Save the filtered data to another CSV file
    filtered_quality_data.to_csv(output_file_3, index=False)
    print(f"Filtered quality data saved to {output_file_3}")



    filtered_quality_data2 = filtered_data[(filtered_data['Golden Reading Image Set Quality'].str.lower() == 'acceptable for diagnosis') &
                                          (filtered_data['Golden Reading Plus'].str.lower() != 'unknown')]

    # Save the filtered data to another CSV file
    filtered_quality_data2.to_csv(output_file_4, index=False)
    print(f"Filtered quality data saved to {output_file_4}")

else:
    print("Error: Required columns 'subjectID' and 'eye' are not present in the input file.")

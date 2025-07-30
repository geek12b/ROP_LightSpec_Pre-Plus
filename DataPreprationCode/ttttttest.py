import pandas as pd

# Define the file path
file_path = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\xlsx_generated\unique_posterior_eye_3_Accept_Image_Exist_Images.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Extract the "subjectID" and "eye" columns
subject_eye_data = df[["subjectID", "eye"]]

# Count unique patients
unique_patients = subject_eye_data["subjectID"].nunique()

# Initialize a counter for total eyes
total_eyes = 0

# Loop over each unique patient
for patient in subject_eye_data["subjectID"].unique():
    # Get all rows for this patient
    patient_data = subject_eye_data[subject_eye_data["subjectID"] == patient]
    
    # Check the number of unique eyes for this patient
    unique_eyes_for_patient = patient_data["eye"].nunique()
    
    # If there is more than one unique eye, count 2 (one for each eye)
    if unique_eyes_for_patient > 1:
        total_eyes += 2
    else:
        total_eyes += 1

# Print the results
print(f"Number of unique patients: {unique_patients}")
print(f"Total count of eyes (with duplicates considered): {total_eyes}")

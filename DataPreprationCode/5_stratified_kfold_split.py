import os
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold

# Define the directory containing the unique_posterior_eye_3_Accept_Image.csv
directory = r"C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\xlsx_generated"
output_directory = os.path.join(directory, "kfolds")
os.makedirs(output_directory, exist_ok=True)

# Define column names for image and target
Image_name = "posterior_id"
Target_Name = "Golden Reading Plus"

# Load the unique_posterior_eye_3_Accept_Image_Exist_Images.csv file
# file_path = os.path.join(directory, "unique_posterior_eye_3_Accept_Image.csv")
file_path = os.path.join(directory, "unique_posterior_eye_3_Accept_Image_Exist_Images.csv")
df = pd.read_csv(file_path)

# Check if the Target_Name column exists for stratification
if Target_Name not in df.columns:
    raise ValueError(f"The dataset must include a '{Target_Name}' column for stratification.")

# Step 1: Stratified split to create a test dataset
# Ensure the test set has the same proportion of targets
test_size = 59  # Number of samples for the test set
remaining_df, test_df = train_test_split(
    df, test_size=test_size, stratify=df[Target_Name], random_state=42
)

# Save the test dataset
test_df.to_csv(os.path.join(output_directory, "testROP_p.csv"), index=False)

# Validate that the test dataset retains the target proportions
print("Test set target distribution:")
print(test_df[Target_Name].value_counts(normalize=True))

# Step 2: Stratified K-Fold Cross-Validation on remaining data
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Loop through StratifiedKFold splits
for fold, (train_index, valid_index) in enumerate(skf.split(remaining_df, remaining_df[Target_Name]), 1):
    train_df = remaining_df.iloc[train_index]
    valid_df = remaining_df.iloc[valid_index]

    # Save the train and validation sets
    train_df.to_csv(os.path.join(output_directory, f"train{fold}.csv"), index=False)
    valid_df.to_csv(os.path.join(output_directory, f"valid{fold}.csv"), index=False)

print("5-fold stratified cross-validation datasets have been created and saved.")

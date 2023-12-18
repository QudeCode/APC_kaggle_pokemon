import pandas as pd

dataset_path = "data/pokemon.csv"
results_path = "results/00_complexity_results.txt"

# Load the dataset
df = pd.read_csv(dataset_path)

# Dataset length
dataset_length = len(df)

# Dataset complexity
difficulty_results = {
    "NaNs": df.isna().sum(),
    "Data types": df.dtypes,
    "Class imbalance (is_legendary)": df['is_legendary'].value_counts(normalize=True),
    "Class imbalance (type1)": df['type1'].value_counts(normalize=True),
    "Class imbalance (type2)": df['type2'].value_counts(normalize=True),
}

# Number of non-numeric columns
non_numeric_columns = df.select_dtypes(exclude=['number']).columns
num_non_numeric_columns = len(non_numeric_columns)

# Save the results to a file
with open(results_path, 'w') as file:
    # Most important results
    file.write(f"------------Most important results:------------\n")
    file.write(f"Dataset length: {dataset_length}\n")
    file.write(f"Columns with NaNs: {difficulty_results['NaNs'].astype(bool).sum()}\n")
    file.write(f"Non-numeric columns: {num_non_numeric_columns}\n\n")

    # Class imbalance
    file.write("------Class imbalance:------\n")
    file.write(f"---is_legendary:---\n{difficulty_results['Class imbalance (is_legendary)']}\n\n")
    file.write(f"---type1:---\n{difficulty_results['Class imbalance (type1)']}\n\n")
    file.write(f"---type2:---\n{difficulty_results['Class imbalance (type2)']}\n\n")

    # Other results
    file.write("------------------Detailed results:------------------\n\n")
    file.write(f"Dataset length: {dataset_length}\n\n")
    
    file.write("NaNs:\n")
    file.write(f"{difficulty_results['NaNs']}\n\n")

    file.write("Data types:\n")
    file.write(f"{difficulty_results['Data types']}\n\n")

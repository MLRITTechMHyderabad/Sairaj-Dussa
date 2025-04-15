import pandas as pd

def load_dataset():
    try:
        df = pd.read_csv("youtube_2025_dataset.csv")
        print("Dataset loaded successfully!")
        print(f"Initial dataset shape: {df.shape}")  # Display the number of rows and columns
        print(df.info())
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def remove_duplicates(df):
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    print(f"Duplicates removed. Rows before: {initial_rows}, Rows after: {df.shape[0]}")
    return df


def handle_missing_values(df):
    print("Missing values per column before handling:")
    print(df.isnull().sum())
    df.fillna("Empty-Cell", inplace=True)
    print("Missing values handled (replaced with 'Empty-Cell').")
    print("Missing values per column after handling:")
    print(df.isnull().sum())
    return df

def correct_data_types(df):
    print("Correcting data types...")
    numeric_columns = [
        'Total Videos', 'Total Subscribers', 'Members Count'
    ]
    for col in numeric_columns:
        if col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors="coerce")
                print(f"Column '{col}' converted to numeric successfully.")
            except Exception as e:
                print(f"Error processing column '{col}': {e}")
        else:
            print(f"Column '{col}' does not exist in the dataset. Skipping.")
    print("Data types corrected.")
    return df

def rename_columns(df):
    columns_to_rename = {
        'Total Videos': 'Total_Video_Count',
        'AI Generated Content (%)': 'AI_Content_Percentage',
        'Metaverse Integration Level': 'Metaverse_Level'
    }
    df.rename(columns={key: value for key, value in columns_to_rename.items() if key in df.columns}, inplace=True)
    print("Columns renamed for clarity.")
    print("Updated column names:")
    print(df.columns)
    return df

def filter_irrelevant_data(df):
    original_count = len(df)
    filtered = False

    if 'Total_Video_Count' in df.columns:
        df = df[df['Total_Video_Count'] >= 100]
        filtered = True
        print(f"Filtered based on 'Total_Video_Count' >= 100. Rows before: {original_count}, Rows after: {len(df)}")

    if 'Avg Video Length (min)' in df.columns:
        df = df[df['Avg Video Length (min)'] >= 20]
        filtered = True
        print(f"Filtered based on 'Avg Video Length (min)' >= 22. Rows before: {original_count}, Rows after: {len(df)}")

    if 'Members Count' in df.columns:
        df = df[df['Members Count'] >= 100000 ]
        filtered = True
        print(f"Filtered based on 'Members Count' >= 100000. Rows before: {original_count}, Rows after: {len(df)}")

    if not filtered:
        print("No relevant columns found for filtering. Skipping data processing.")

    return df


def save_cleaned_dataset(df):
    try:
        if df.empty:
            print("Warning: Dataset is empty. Not saving an empty file.")
        else:
            df.to_csv("cleaned_youtube_2025_dataset.csv", index=False)
            print("Cleaned dataset saved to 'cleaned_youtube_2025_dataset.csv'.")
    except Exception as e:
        print(f"Error saving dataset: {e}")

def main():
    print("Welcome to the YouTube 2025 Data Cleaning Application!")
    
    dataset = load_dataset()
    if dataset is None or dataset.empty:
        print("Dataset loading failed or dataset is empty. Exiting application.")
        return

    while True:
        print("\nSelect an operation to perform Data Cleaning:")
        print("1. Remove duplicates")
        print("2. Handle missing values")
        print("3. Correct data types")
        print("4. Rename columns")
        print("5. Filter irrelevant data")
        print("6. Save cleaned dataset")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-7.")
            continue

        if choice == 1:
            dataset = remove_duplicates(dataset)
        elif choice == 2:
            dataset = handle_missing_values(dataset)
        elif choice == 3:
            dataset = correct_data_types(dataset)
        elif choice == 4:
            dataset = rename_columns(dataset)
        elif choice == 5:
            dataset = filter_irrelevant_data(dataset)
        elif choice == 6:
            save_cleaned_dataset(dataset)
        elif choice == 7:
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
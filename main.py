import pandas as pd
import io

def sort_csv_by_column(input_csv_path, output_csv_path, column_to_sort_by):
    """
    Reads a CSV file, sorts it by a specified column, and saves the sorted data to a new CSV file.

    Args:
        input_csv_path (str): The path to the input CSV file.
        output_csv_path (str): The path where the sorted CSV file will be saved.
        column_to_sort_by (str): The name of the column to sort by.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_csv_path)
        print(f"Original data from '{input_csv_path}':")
        print(df)
        print("-" * 30)

        # Check if the column exists
        if column_to_sort_by not in df.columns:
            print(f"Error: Column '{column_to_sort_by}' not found in the CSV file.")
            print(f"Available columns are: {', '.join(df.columns)}")
            return

        # Sort the DataFrame by the specified column
        # inplace=True modifies the DataFrame directly
        df.sort_values(by=column_to_sort_by, inplace=True)

        print(f"Data sorted by '{column_to_sort_by}':")
        print(df)
        print("-" * 30)

        # Save the sorted DataFrame to a new CSV file
        # index=False prevents pandas from writing the DataFrame index as a column
        df.to_csv(output_csv_path, index=False)
        print(f"Sorted data successfully saved to '{output_csv_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_csv_path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{input_csv_path}' is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Example Usage ---

# 1. Create a dummy CSV file for demonstration
# In a real scenario, you would have an existing CSV file.
# We'll simulate one using io.StringIO for this example.
csv_content = """Name,Age,Section,Dept
Alice,30,A,HR
Bob,24,B,IT
Charlie,28,A,Finance
David,22,C,HR
Eve,26,B,IT
"""

# Define input and output file paths
input_file = "students.csv"
output_file = "students_sorted_by_name.csv"
column_to_sort = "Name" # Change this to "Age", "Section", or "Dept" to sort by other columns

# Write the dummy content to the input file
try:
    with open(input_file, 'w') as f:
        f.write(csv_content)
    print(f"Created a dummy CSV file: '{input_file}'")
except IOError as e:
    print(f"Could not write dummy CSV file: {e}")

# Call the function to sort the CSV
sort_csv_by_column(input_file, output_file, column_to_sort)

# --- Another Example: Sorting by Age ---
print("\n--- Sorting by Age Example ---")
output_file_age = "students_sorted_by_age.csv"
column_to_sort_age = "Age"
sort_csv_by_column(input_file, output_file_age, column_to_sort_age)


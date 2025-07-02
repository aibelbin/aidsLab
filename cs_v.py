import csv

csv_file = 'test.csv'

# Read the CSV file into a list
with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

# Separate header and data rows
header = data[0]
rows = data[1:]

# Find the index of the "Name" column
name_index = header.index("Name")

# Sort the data based on the "Name" column
sorted_rows = sorted(rows, key=lambda row: row[name_index])

# Print sorted data
print("Sorted by Name:")
print(header)
for row in sorted_rows:
    print(row)

print("-------------------------------------------------")

# Print original data
print("Original Content:")
print(header)
for row in rows:
    print(row)

import csv


csv_file = 'test.csv'

with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]
rows = data[1:]

name_index = header.index("Name")

sorted_rows = sorted(rows, key=lambda row: row[name_index])

print("Sorted by Name:")
print(header)
for row in sorted_rows:
    print(row)

print("-------------------------------------------------")


print("Original Content:")
print(header)
for row in rows:
    print(row)

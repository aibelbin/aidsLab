import pandas as pd 

csv = 'test.csv'

file_content = pd.read_csv(csv)
file_sorted = file_content.sort_values(by="Name")

print(file_sorted)
print("-------------------------------------------------")
print(file_content)
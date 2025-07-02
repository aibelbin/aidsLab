import pandas as pd 

csv = 'test.csv'

file_content = pd.read_csv(csv)

print(file_content)
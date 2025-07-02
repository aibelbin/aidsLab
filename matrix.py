rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

def newMatrix(matrix, rows, columns):
    print("\nEnter values for the matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            val = int(input(f"Enter value for ({i+1},{j+1}): "))
            row.append(val)
        matrix.append(row)

def addMatrix(matrix1):
    print("\nEnter values for the matrix to add:")
    matrix2 = []
    for i in range(rows):
        row = []
        for j in range(columns):
            val = int(input(f"Enter value for ({i+1},{j+1}): "))
            row.append(val)
        matrix2.append(row)

    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    print("\nResult of Addition:")
    for row in result:
        print(row)

def subtractMatrix(matrix1):
    print("\nEnter values for the matrix to subtract:")
    matrix2 = []
    for i in range(rows):
        row = []
        for j in range(columns):
            val = int(input(f"Enter value for ({i+1},{j+1}): "))
            row.append(val)
        matrix2.append(row)

    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    print("\nResult of Subtraction:")
    for row in result:
        print(row)

newMatrix(matrix, rows, columns)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

addMatrix(matrix)
subtractMatrix(matrix)

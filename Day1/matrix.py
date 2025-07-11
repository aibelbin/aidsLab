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

def multiplyMatrix(matrix1):
    print("\nEnter values for the matrix to multiply:")
    matrix2 = []
    for i in range(columns):  # must match matrix1's columns
        row = []
        for j in range(columns):
            val = int(input(f"Enter value for ({i+1},{j+1}): "))
            row.append(val)
        matrix2.append(row)

    result = []
    for i in range(rows):
        row = []
        for j in range(columns):
            val = 0
            for k in range(columns):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        result.append(row)

    print("\nResult of Multiplication:")
    for row in result:
        print(row)


newMatrix(matrix, rows, columns)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

addMatrix(matrix)
subtractMatrix(matrix)
multiplyMatrix(matrix)

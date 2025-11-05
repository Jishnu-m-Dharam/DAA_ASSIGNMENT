n = int(input("Enter the size of the matrix (n): "))
matrix = []
for i in range(n):
    row=[]
    for j in range(n):
        value = int(input(f"Enter value for position [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)
print("Matrix:")
for row in matrix:
    print(row)
i = int(input("Enter row index (starting from 0): "))
j = int(input("Enter column index (starting from 0): "))
print("Value at position [", i, "][", j, "] is:", matrix[i][j])

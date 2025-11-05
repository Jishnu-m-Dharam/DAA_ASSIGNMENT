
def get_matrix_from_user(name, rows, cols):
    print(f"\nEnter elements for Matrix {name} ({rows} rows x {cols} cols):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    val = float(input(f"  Enter element {name}[{i+1}][{j+1}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("  Invalid input. Please enter a number.")
        matrix.append(row)
    return matrix

def print_matrix(matrix, name):
    print(f"\n--- Matrix {name} ---")
    if not matrix:
        print("[]")
        return

    for row in matrix:
        print("  [", end="")
        for val in row:
            print(f"{val:8.2f}", end=" ")
        print("]")

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return None

    C = []
    for i in range(rows_A):
        row = [0] * cols_B
        C.append(row)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(rows_B):
                C[i][j] += A[i][k] * B[k][j]

    return C

def main():
    while True:
        try:
            rows_A = int(input("\nEnter rows for Matrix A: "))
            cols_A = int(input("Enter columns for Matrix A: "))
            if rows_A > 0 and cols_A > 0:
                break
            else:
                print("Dimensions must be positive integers.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    while True:
        try:
            rows_B = int(input("\nEnter rows for Matrix B: "))
            cols_B = int(input("Enter columns for Matrix B: "))
            if rows_B > 0 and cols_B > 0:
                break
            else:
                print("Dimensions must be positive integers.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    if cols_A != rows_B:
        print("\nError: Cannot multiply matrices.")
        print(f"Columns of A ({cols_A}) must equal rows of B ({rows_B}).")
        return

    A = get_matrix_from_user("A", rows_A, cols_A)
    B = get_matrix_from_user("B", rows_B, cols_B)

    C = multiply_matrices(A, B)

    print_matrix(A, "A")
    print_matrix(B, "B")
    print_matrix(C, "C (Result A * B)")

if __name__ == "__main__":
    main()
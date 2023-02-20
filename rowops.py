from matrix import Matrix


def load_matrix_file(filename: str) -> Matrix:
    with open(filename) as f:
        rows = f.readlines()
    matrix = Matrix(shape=(len(rows), len(rows[0].split())))
    for i, row in enumerate(rows):
        for j, value in enumerate(row.split()):
            matrix[i, j] = float(value)
    return matrix

def load_matrix_cli() -> Matrix:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = Matrix(shape=(rows, columns))
    for i in range(rows):
        input = input(f"Enter row {i + 1}: ").split()
        for j, value in enumerate(input):
            matrix[i, j] = float(value)
    return matrix

def write_matrix_file(filename: str, matrix: Matrix) -> None:
    with open(filename, "w") as f:
        for i in range(matrix.rows):
            for j in range(matrix.columns):
                f.write(str(matrix[i, j]) + " ")
            f.write("\n")

def main() -> None:
    matrix: Matrix = None # type: ignore
    while(True):
        print("1. Swap rows")
        print("2. Scale row")
        print("3. Add row")
        print("4. Load from file")
        print("5. Load from CLI")
        print("6. Write to file")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            if matrix is None:
                print("No matrix loaded")
                continue
            row1 = int(input("Enter row 1: "))
            row2 = int(input("Enter row 2: "))
            matrix.swap(row1-1, row2-1)
        elif choice == 2:
            if matrix is None:
                print("No matrix loaded")
                continue
            row = int(input("Enter row: "))
            scalar = float(input("Enter scalar: "))
            matrix.scale_row(row-1, scalar)
        elif choice == 3:
            if matrix is None:
                print("No matrix loaded")
                continue
            scalar1 = float(input("Enter scalar 1: "))
            row1 = int(input("Enter row 1: "))
            scalar2 = float(input("Enter scalar 2: "))
            row2 = int(input("Enter row 2: "))
            out_row = int(input("Enter output row: "))
            matrix.add_row(row1-1, row2-1, out_row-1, scalar1, scalar2)
        elif choice == 4:
            filename = input("Enter filename: ")
            matrix = load_matrix_file(filename)
        elif choice == 5:
            matrix = load_matrix_cli()
        elif choice == 6:
            if matrix is None:
                print("No matrix loaded")
                continue
            filename = input("Enter filename: ")
            write_matrix_file(filename, matrix)
        elif choice == 7:
            break
        else:
            print("Invalid choice")
        print(matrix)

if __name__ == "__main__":
    main()

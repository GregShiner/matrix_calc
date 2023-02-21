from matrix import Matrix
from fractions import Fraction
import help


def load_matrix_file(filename: str) -> Matrix:
    with open(filename) as f:
        rows = f.readlines()
    matrix = Matrix(shape=(len(rows), len(rows[0].split())), dtype=Fraction)
    for i, row in enumerate(rows):
        for j, value in enumerate(row.split()):
            matrix[i, j] = Fraction(value)
    return matrix

def load_matrix_cli() -> Matrix:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = Matrix(shape=(rows, columns), dtype=Fraction)
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        if len(row) != columns:
            raise ValueError()
        for j, value in enumerate(row):
            matrix[i, j] = Fraction(value)
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
        print("7. Help")
        print("8. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except Exception as e:
            print("An unknown error has occurred. Please try again.")
            print(e)
            continue
        if choice == 1:
            try:
                if matrix is None:
                    print("No matrix loaded")
                    continue
                row1 = int(input("Enter row i: "))
                row2 = int(input("Enter row j: "))
                matrix.swap(row1-1, row2-1)
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
                print(e)
        elif choice == 2:
            try:
                if matrix is None:
                    print("No matrix loaded")
                    continue
                row = int(input("Enter row: "))
                scalar = Fraction(input("Enter scalar: "))
                matrix.scale_row(row-1, scalar)
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
                print(e)
        elif choice == 3:
            try:
                if matrix is None:
                    print("No matrix loaded")
                    continue
                scalar1 = Fraction(input("Enter scalar for row i: "))
                row1 = int(input("Enter row i: "))
                scalar2 = Fraction(input("Enter scalar for row j: "))
                row2 = int(input("Enter row j: "))
                out_row = int(input("Enter output row: "))
                if (out_row != row1) or (out_row != row2):
                    print("The output row must be either i or j")
                    continue
                matrix.add_row(row1-1, row2-1, out_row-1, scalar1, scalar2)
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
                print(e)
        elif choice == 4:
            filename = input("Enter filename: ")
            try:
                matrix = load_matrix_file(filename)
            except FileNotFoundError:
                print("File not found. Please try again.")
            except Exception as e:
                print("An unknown error occurred, please try again.:")
                print(e)
        elif choice == 5:
            try:
                matrix = load_matrix_cli()
            except ValueError as e:
                print("You did not input the correct number of values")
            except Exception as e:
                print("An unknown error occurred, please try again.:")
                print(e)
        elif choice == 6:
            try:
                if matrix is None:
                    print("No matrix loaded")
                    continue
                filename = input("Enter filename: ")
                write_matrix_file(filename, matrix)
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
                print(e)
        elif choice == 7:
            choice = input("Select an option number to view help for that option, or enter -1 to get help for the entire program: ")
            try:
                choice = int(choice)
                if choice == -1:
                    print(help.help())
                else:
                    print(help.option_help(choice))
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
        elif choice == 8:
            break
        else:
            print("Invalid choice")
        if matrix: print(matrix)

if __name__ == "__main__":
    main()

from matrix import Matrix
from fractions import Fraction
from rowops import load_matrix_file, load_matrix_cli, write_matrix_file

def simplex_iteration(matrix: Matrix) -> Matrix:
    # find pivot column
    pivot_column = 0
    # for each column except the last
    # TODO: check if this needs to be -2
    for i in range(matrix.columns - 1):
        # if the value in the last row is less than the current minimum
        if matrix[matrix.rows - 1, i] < matrix[matrix.rows - 1, pivot_column]:
            pivot_column = i
    # find pivot row
    # find the row with the minimum non-negative ratio of matrix[i, matrix.columns - 1] / matrix[i, pivot_column]
    theta_ratios = []
    for i in range(matrix.rows - 1): # Don't check the objective function row
        if matrix[i, pivot_column] == 0:
            theta_ratios.append((i, float('inf')))
        else:
            theta_ratios.append((i, matrix[i, matrix.columns - 1] / matrix[i, pivot_column]))
    theta_ratios = list(filter(lambda x: x[1] >= 0, theta_ratios))
    if len(theta_ratios) == 0:
        print("Unbounded solution")
        return matrix
    pivot_row = min(theta_ratios, key=lambda x: x[1])[0]
    
    # scale pivot row
    print(f"R{pivot_row + 1} / {matrix[pivot_row, pivot_column]} -> R{pivot_row + 1}")
    matrix.scale_row(pivot_row, Fraction(1, matrix[pivot_row, pivot_column]))
    # print the row op
    # scale other rows
    for i in range(matrix.rows):
        if i == pivot_row:
            continue
        print(f"{-matrix[i, pivot_column]} * R{pivot_row + 1} + R{i + 1} -> R{i + 1}")
        matrix.add_row(pivot_row, i, i, Fraction(-matrix[i, pivot_column]), Fraction(1))
    return matrix

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
        print("8. Simplex")
        print("9. Exit")
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
                if not ((out_row != row1) or (out_row != row2)):
                    print("The output row must be either i or j")
                    continue
                matrix.add_row(row1-1, row2-1, out_row-1, scalar1, scalar2)
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
                print(e)
        elif choice == 4:
            filename = input("Enter filename: ") or "matrix.txt"
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
            try:
                with open("helptext.txt", "r") as f:
                    print(f.read())
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
        elif choice == 8:
            try:
                if matrix is None:
                    print("No matrix loaded")
                    continue
                while(True):
                    print(matrix)
                    choice = input("Enter 'n' to continue, or 'q' to quit: ")
                    if choice == 'n':
                        matrix = simplex_iteration(matrix)
                    elif choice == 'q':
                        break
                    else:
                        print("Invalid choice")
            except Exception as e:
                print("An unknown error has occurred. Please try again.")
                print(e)
        elif choice == 9:
            break
        else:
            print("Invalid choice")
        print(matrix)

if __name__ == "__main__":
    main()
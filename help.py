def help():
    return """Welcome to the matrix calculator.
Intro:
To use the calculator, first load a matrix. You can load a matrix via file (option 4) or by typing it in inside the command line (option 5).
You can select an option when given the prompt "Enter you choice: " preceded by the list of options. 
Simply type the corresponding number and hit enter.

File Loading (4):
The file to load should be plain text and consist of either decimal numbers, or fractions (ex: 7, 4.32 or 2/3).
These values in a row should be separated by a single space, and each row should be separated by a new line (example matrix.txt file on github).
When prompted, enter the name of the file to load.
You can also enter a relative path to a file.

CLI Loading (5):
To load values via the command line, follow the prompts for number of rows and columns, then enter the values in each row when prompted.
The rows should be written exactly the same as in the file loading mode.

Operations:
Once a matrix has been loaded, you can begin doing operations.
After each operation (including loading) the matrix will be printed.
Whenever you do any operation, the result will be loaded, allowing you to do multiple operations without reloading every time

Row Swap (1):
The row swap operation swaps Rows Ri and Rj.
When prompted, enter the number of the row corresponding to Ri and Rj respectively

Scale Row (2):
The scale row operation multiplies each element in a row by a constant scalar
First, enter the number of the row to scale
Then enter the scalar to multiply by. This can be an integer, decimal, or fraction

Add Row (3):
This operation does S1(Ri) + S2(Rj) -> Ri (or Rj)
First input the scalar to multiply Ri by
Then input the row number for Ri
Then input the scalar to multiple Rj by
Then input the row number for Rj
Finally input the row number for the output (must be either Ri or Rj)

Write to File (6):
This option will write the current matrix to a file that can be imported later.
Simply enter the name of the output file
"""
def option_help(option: int) -> str:
    if option == 1:
        return """Row Swap (1):
The row swap operation swaps Rows Ri and Rj.
When prompted, enter the number of the row corresponding to Ri and Rj respectively"""
    elif option == 2:
        return """Scale Row (2):
The scale row operation multiplies each element in a row by a constant scalar
First, enter the number of the row to scale
Then enter the scalar to multiply by. This can be an integer, decimal, or fraction"""
    elif option == 3:
        return """Add Row (3):
This operation does S1(Ri) + S2(Rj) -> Ri (or Rj)
First input the scalar to multiply Ri by
Then input the row number for Ri
Then input the scalar to multiple Rj by
Then input the row number for Rj
Finally input the row number for the output (must be either Ri or Rj)"""
    elif option == 4:
        return """File Loading (4):
The file to load should be plain text and consist of either decimal numbers, or fractions (ex: 7, 4.32 or 2/3).
These values in a row should be separated by a single space, and each row should be separated by a new line (example matrix.txt file on github).
When prompted, enter the name of the file to load.
You can also enter a relative path to a file."""
    elif option == 5:
        return """CLI Loading (5):
To load values via the command line, follow the prompts for number of rows and columns, then enter the values in each row when prompted.
The rows should be written exactly the same as in the file loading mode."""
    elif option == 6:
        return """Write to File (6):
This option will write the current matrix to a file that can be imported later.
Simply enter the name of the output file"""
    else:
        return "Invalid option"
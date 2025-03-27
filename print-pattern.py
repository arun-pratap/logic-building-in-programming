"""
Write a function named print_pattern that prints a rectangle pattern of stars (*).

The function should:

Take two parameters: rows and cols (both integers)
Use nested loops to print a rectangle with the given dimensions
Each row should contain cols stars
The pattern should have rows rows in total
Example output for print_pattern(3, 4):

****
****
****
"""

# first approach
def print_pattern(rows,cols):
    for rows in range(1, rows +1):
        temp = ""
        for cols  in range(1, cols + 1):
            temp += "*"
        print(temp)   
print_pattern(4,2)

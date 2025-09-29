# Matrix

# Overview
This repository contains Python classes that demonstrate various matrix manipulation operations and a physics calculation implementation. The code showcases object-oriented programming concepts including inheritance and method overriding.

# 1. Physics Calculation Classes
Purpose: Calculates energy using Einstein's mass-energy equivalence formula

Attributes:
-c: celerity (speed)
-m: mass (weight)

Methods:
-energy(): Returns calculated energy using E = mc²
printing Class (inherits from pythonCode)
Purpose: Displays the calculated energy in a formatted way

Methods:
-print_energy(): Prints the energy value with decorative borders

# 2. Matrix Manipulation Classes
matrix Class
-Purpose: Base class for matrix operations
-Attributes:
    n: number of rows
    m: number of columns

matrix_print Class (inherits from matrix)
-Purpose: Provides various matrix manipulation and display methods
-Key Methods:
    print_matrix(): Generates a random matrix with values between 1-9
    matrix_with_for(): Displays the original matrix
    diagonal_with_zero(): Sets diagonal elements to 0 and displays matrix
    down_diagonal_with_zero(): Sets elements below diagonal to 0
    up_diagonal_with_zero(): Sets elements above diagonal to 0
    up_diagonal_with_sign_down(): Replaces elements above diagonal with '-'
    up_diagonal_with_sign_up(): Replaces elements below diagonal with '-'

# Features
-Random Matrix Generation: Creates matrices with random integer values
-Diagonal Manipulations: Various methods to modify matrix diagonals
-Formatted Output: Clean, readable matrix displays with separators
-Physics Integration: Combines scientific calculation with matrix operations

# Usage Example
#Physics calculation
obj = printing(9, 3.9)
obj.print_energy()

#Matrix operations
obj1 = matrix_print(12, 12)
obj1.matrix_with_for()
obj1.diagonal_with_zero()
obj1.down_diagonal_with_zero()
#... other matrix methods

# Output Format
The code produces formatted output with:
-48-character wide separators (-)
-Clear labeling for each operation
-Readable matrix displays with proper spacing

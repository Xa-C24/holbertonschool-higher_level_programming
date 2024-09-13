#!/usr/bin/python3
"""
Module for dividing all elements of a matrix by a divisor
"""
def matrix_divided(matrix, div):
    if matrix == [] or matrix == [[]]:
        return []
    
    if not isinstance(matrix, list) or len(matrix) == 0 or not all (isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError ("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

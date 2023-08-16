#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        matrix = []
    return [[x: x ** 2 for x in row] for row in matrix]

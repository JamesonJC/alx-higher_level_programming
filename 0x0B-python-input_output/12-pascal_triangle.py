#!/usr/bin/python3
''' A Pascal's Triangle.'''


def pascal_triangle(n):
    '''
    Function Pascal's Triangle of size n as a list of lists.

    Args:
        n (int): Rows to generate for the Pascal's Triangle

    Returns:
        list: List of lists.

    '''

    if n <= 0:
        return []

    triangles = [[1]]

    while len(triangles) != n:
        lst_row = triangles[-1]
        new_row = [1]
        
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        triangles.append(new_row)
    return (triangles)

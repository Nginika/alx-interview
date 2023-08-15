#!/usr/bin/python3
"""
This function takes a 2d matrix and rotates it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    transposed = []
    for i in range(n):
        x = n - 1
        inner_list = []
        for j in range(n):
            inner_list.append(matrix[x][i])
            x = x - 1
        transposed.append(inner_list)

    # Update the original matrix with the rotated values
    for i in range(n):
        for j in range(n):
            matrix[i][j] = transposed[i][j]

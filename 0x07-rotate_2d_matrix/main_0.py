#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 0, 7, 9],
              [4, 5, 6, 5, 2, 8],
              [7, 8, 9, 4, 2, 1],
              [0, 9, 8, 7, 6, 5],
              [4, 3, 2, 1, 1, 9],
              [2, 8, 3, 7, 4, 6]]

    rotate_2d_matrix(matrix)
    print(matrix)

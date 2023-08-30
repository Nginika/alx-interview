#!/usr/bin/python3
""" calculates the perimeter of an island"""


def island_perimeter(grid):
    count = 0
    for meter in grid:
        for square in meter:
            if square == 1:
                count = count + 1
    perimeter = (2 * count) + 2
    return perimeter

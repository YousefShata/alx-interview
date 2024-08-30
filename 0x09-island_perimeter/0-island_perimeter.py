#!/usr/bin/python3
"""
island model
"""


def island_perimeter(grid):
    """
    island premieter func
    """
    if not grid:
        return 0

    perimeter = 0
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for y in range(col):
            if grid[i][y] == 1:
                if i == 0 or grid[i-1][y] == 0:
                    perimeter += 1
                if i == row-1 or grid[i+1][y] == 0:
                    perimeter += 1
                if y == 0 or grid[i][y-1] == 0:
                    perimeter += 1
                if y == col-1 or grid[i][y+1] == 0:
                    perimeter += 1

    return perimeter

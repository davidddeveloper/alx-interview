#!/usr/bin/python3
"""
    0-island_perimeter.py: Island Perimeter

"""


def island_perimeter(grid):
    """ perimeter of the island describe in grid
        Args:
            - grid: list of list of integers:
                - 0 represents water
                - 1 represents land

    """

    # (index of row, index of col)
    vertical_start = (0, 0)
    vertical_end = (0, 0)

    horizontal_start = (0, 0)
    horizontal_end = (0, 0)

    for index, row in enumerate(grid):
        for idx, col in enumerate(row):
            if col == 1 and vertical_start == (0, 0):
                vertical_start = (index, idx)
                horizontal_start = (index, idx)

            if col == 1:
                vertical_end = (index, idx)
                horizontal_end = (index, idx)

    # since each cell is a square we multiply by 4
    perimeter = (
        (horizontal_end[0] - vertical_start[0]) + 1
    ) * 4  # add 1 for inclusivity

    return perimeter

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

    if vertical_start == (0, 0) and horizontal_start == (0, 0) \
            and vertical_end == (0, 0) and horizontal_end == (0, 0):
        return 0  # no island

    # we are adding 1 for inclusivity
    vertical_length = ((vertical_end[0] - vertical_start[0]) + 1)
    horizontal_length = ((horizontal_end[1] - horizontal_start[0]) + 1)

    # since each cell is a square we multiply by 2
    vertical_length = vertical_length * 2
    horizontal_length = horizontal_length * 2

    perimeter = (vertical_length + horizontal_length)

    return perimeter

#!/usr/bin/python3
"""
    0-pascal_triangle: Represents a pascal triangle

"""

def pascal_triangle(n):
    """ generate a pascal triangle base on the n

        - n: the height or number of row in the computed pascal triangle

    """

    pascal_tri = []
    if n <= 0:
        return pascal_tri

    prev_row = []
    for i in range(n):
        j = 0
        row = []
        while j <= i:
            if j == 0 or j == i:
                row.append(1)
            else:
                column = prev_row[j] + prev_row[j - 1]
                row.append(column)
            j += 1
        pascal_tri.append(row)
        prev_row = row

    return pascal_tri

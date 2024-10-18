#!/usr/bin/python3
"""
    rotate_2d_matrix.py: Rotate a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    :param matrix: 2D matrix to rotate
    :return: rotated matrix
    """
    n = len(matrix)

    # Loop through each layer (starting from outer to inner)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        # Loop through the elements in the current layer
        for i in range(first, last):
            # Save the top element
            offset = i - first
            top = matrix[first][i]  # top element

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = top

    return matrix

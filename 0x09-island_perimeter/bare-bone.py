grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

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
perimeter = ((horizontal_end[0] - vertical_start[0]) + 1) * 4 # add 1 for inclusivity

print(vertical_start, horizontal_start)
print(vertical_end, horizontal_end)

print(perimeter)
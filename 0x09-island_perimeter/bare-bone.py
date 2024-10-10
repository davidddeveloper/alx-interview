grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
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

if vertical_start == (0, 0) and horizontal_start == (0, 0) \
        and vertical_end == (0, 0) and horizontal_end == (0, 0):
    print('no island')
    exit(0)

# since each cell is a square we multiply by 4
vertical_length = ((vertical_end[0] - vertical_start[0]) * 2) + 1
horizontal_length = ((horizontal_end[1] - horizontal_start[0]) * 2) + 1

print(vertical_length, horizontal_length)

perimeter = (vertical_length + horizontal_length)  # add 1 for inclusivity

print(vertical_start, horizontal_start)
print(vertical_end, horizontal_end)

print(perimeter)

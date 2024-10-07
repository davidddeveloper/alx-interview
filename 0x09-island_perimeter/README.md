# Island Perimeter
>`question`: find the perimeter of the island described in `grid`:
>
> `grid`: is a list of integers
> - 0 represents water
> - 1 represents land
> - Each cell is square, with a side length of 1
> - Cells are connected horizontally/vertically (not diagonally).
> - grid is rectangular, with its width and height not exceeding 100
>
> - The grid is completely surrounded by water
> - There is only one island (or nothing)
> - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)
>
  > prototype: `def island_perimeter(grid)`

>`idea`: the simplest way to solve this problem is to find the start and end of the island and multiple it by 4.
>
>`how to do this`: since 1 represent water, loop through the array and save the row index and column index when you first find 1. Do this when you find last find 1, subtract and multiple by 4 to find perimeter. Look at the pseudocode below to further undestand this concept.
>

>`goal`: find the perimeter in a 2d list



## pseudocode
    vertical_start = (0, 0) 
    horizontal_start = (0, 0)
    vertical_end = (0, 0) 
    horizontal_end = (0, 0)
    
    row: loop through the list
        col: loop through row
            if col == 1 and vertical_start is empty:
                vertical_start = (row_idx, col_idx)
                horizontal_start = (row_idx, col_idx)
            
            if col == 1:
                vertical_end = (row_idx, col_idx)
                horizontal_end = (row_idx, col_idx)
        
        perimeter:
            subtract horizontal_end from vertical_end
            add 1
            multiply by 4


## solution
> [python](0-island_perimeter.py)

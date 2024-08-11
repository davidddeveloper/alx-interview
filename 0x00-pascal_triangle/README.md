# Pascal's Triangle

pascal triangle are numbers arrange in triangular way such that one is at the first row, 1s are at the both ends of the other rows and the other numbers in the other columns are obtained by adding the nearest numbers in the top row.
## pseudocode
```
  prevrow = row
  loop five times:
      row = []
      loop base on the index of the upper loop: # ie if upper is at index 0 loop once index 1 loop twice and so on
      if loop is at index 0:
          append 1 to the row

      elif loop index is equal to upper loop index:
          append 1 to the row

      else # we are at the other columns
          column = [get current index in prevrow] + [get current index - 1 in prevrow]
          append column to the row
      print(row)
      prevrow = row
	
```

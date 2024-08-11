# Pascal's Triangle

Pascal triangle are numbers arrange in triangular way such that one is at the first row, 1s are at the both ends of the other rows and the other numbers in the other columns are obtained by adding the nearest numbers in the top row.

![pascals-triangle](https://github.com/user-attachments/assets/24cd8687-7d11-41a9-ae81-e55dd466d3cf)

## pseudocode
```

loop five times:
row = []
loop base on the index of the upper loop: # ie if upper is at index 0 loop once index 1 loop twice and so on
if loop is at index 0:
  append 1 to the row

elif loop index is equal to upper loop index: # meaning we are at the end of the row
  append 1 to the row

else # we are at the other columns # meanint we are somewhere in between the row
  column = [get current index in prevrow] + [get current index - 1 in prevrow]
  append column to the row
print(row)
prevrow = row
	
```

#!/usr/bin/python3
"""
    0-minoperations: iterative approach with file read/write to find the minimum number operations
    to result in nHs
    read the readme for explanation at github:
    davidddeveloper/alx-interview/blob/main/0x02-minimum_operations/README.md
	Note: this is very inefficient especially with larger values of n

"""


def minOperations(n):
    no_of_operation = 0
    if n == 1:
        return 1

    # initially create the file
    with open('xyz', 'w') as f:
    	f.write('H')  # paste

    counter = 2
    while (counter <= n):
        if n % counter == 0:  # counter is a factor of n
            print(counter, n)
            no_of_operation += counter

            # perform the read and write operation
            copied = 'character'
            for i in range(counter):
				if i == 0:
					with open('xyz', 'r') as f:
						copied = f.read()

                 else:
					 with open('xyz', 'a') as f:
						 f.write(copied)

            n = n // counter
            counter = 2  # reset counter
        else:
            counter += 1

    return no_of_operation

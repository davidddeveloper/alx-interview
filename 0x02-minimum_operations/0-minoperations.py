#!/usr/bin/python3
"""
    0-minoperations.py: Recursive approach to find Minimum Operations
    to result in nHs

    read the readme for explanation at github:
    davidddeveloper/alx-interview/blob/main/0x02-minimum_operations/README.md

"""


def minOperations(n):
    no_of_operation = 0
    if n == 1:
        # initially create the file
        # with open('xyz', 'w') as f:
        #    f.write('H')  # paste
        return no_of_operation

    # dynamic programming - tabulation
    for i in range(2, n + 1):
        if n % i == 0:
            no_of_operation += minOperations(n // i)
            no_of_operation += i

            # perform the read and write operation
            # copied = 'character'
            # for i in range(i):
            #    if i == 0:
            #        with open('xyz', 'r') as f:
            #            copied = f.read()

            #    else:
            #        with open('xyz', 'a') as f:
            #            f.write(copied)

            break

    return no_of_operation

#!/usr/bin/python3
"""
    0-minoperations: iterative approach to find the minimum number operations
    to result in nHs
    read the readme for explanation at github:
    davidddeveloper/alx-interview/blob/main/0x02-minimum_operations/README.md

"""


def minOperations(n):
    operation_count = 0
    if n == 1:
        return operation_count

    counter = 2
    while (counter <= n):
        while n % counter == 0:  # counter is a factor of n
            operation_count += counter

            n = n // counter
        counter += 1

    return operation_count

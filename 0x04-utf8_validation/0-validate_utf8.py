#!/usr/bin/python3
"""
    this code checks if a data is a valid utf-8 encoded
    len(bin(number).split('0b')[1]) > 7
    if number < 32 or number > 128
"""


def validUTF8(data):
    if data == []:
        return False

    for number in data:
        if number > 128:
            return False
    return True

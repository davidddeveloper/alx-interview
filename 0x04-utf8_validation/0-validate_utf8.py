#!/usr/bin/python3
"""
    this code checks if a data is a valid utf-8 encoded
"""


def validUTF8(data):
    if data == []:
        return False

    for number in data:
        if number >= 32 and <= 127:
            return False
    return True

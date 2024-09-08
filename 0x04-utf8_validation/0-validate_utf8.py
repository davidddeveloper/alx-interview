#!/usr/bin/python3
"""
    this code checks if a data is a valid utf-8 encoded
"""


def validUTF8(data):
    for number in data:
        if number > 255:
            return False
    return True

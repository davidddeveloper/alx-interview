#!/usr/bin/python3
"""
    0-making_change.py: minimum set of coins needed to make a change
"""


def makeChange(coins, total):
    """
        return the minimum set of coins needed
        to make a change to a total
    """
    dp = coins
    dp.sort()
    count = 0

    i = len(dp)
    while i >= 0:
        if dp[i - 1] <= total:
            total = total - dp[i - 1]
            count += 1
        elif total == 0:
            break
        else:
            i = i - 1

    return count


print(makeChange([1, 2, 25], 37))

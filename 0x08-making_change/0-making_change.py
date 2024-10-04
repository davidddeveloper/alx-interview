#!/usr/bin/python3
"""
    0-making_change.py: minimum set of coins needed to make a change
"""


def makeChange(coins, total):
    """
        return the minimum set of coins needed
        to make a change to a total
    """
    if total <= 0:
        return 0

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

    # meaning: i can't change total with the coins have
    if total != 0:
        return -1

    return count

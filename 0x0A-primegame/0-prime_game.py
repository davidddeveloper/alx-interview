#!/usr/bin/python3
"""
    0-prime_game: find the winner in a game of two players
    given a set of numbers, players take turn
    choosing a prime number removing it and it multiples
"""


def prime_numbers(n):
    """
    Find the prime numbers from 2 to n (inclusive).
    """
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    prime_nums = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_nums.append(p)
    return prime_nums


def remove_multiples(prime, prime_numbers):
    """
    Remove multiples of the prime number from the list of prime numbers.
    """
    return [num for num in prime_numbers if num % prime != 0]


def isWinner(x, nums):
    """
    Determines the winner of the game.
    """
    player_one_point = 0
    player_two_point = 0
    last_player = None

    for n in nums:
        prime_nums = prime_numbers(n)
        player_one_turns = True

        # Alternate between players
        while prime_nums:
            current_prime = prime_nums[0]
            prime_nums = remove_multiples(current_prime, prime_nums)

            if player_one_turns:
                player_one_point += 1
                player_one_turns = False
                last_player = 'Maria'
            else:
                player_two_point += 1
                player_one_turns = True
                last_player = 'Ben'

    # Determine the winner
    if player_one_point > player_two_point:
        return 'Maria'
    elif player_two_point > player_one_point:
        return 'Ben'
    else:
        return last_player

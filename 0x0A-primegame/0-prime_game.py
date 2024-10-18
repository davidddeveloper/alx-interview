#!/usr/bin/python3

def prime_numbers(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] is True:

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    prime_nums = []
    for p in range(2, n+1):
        if prime[p]:
            prime_nums.append(p)
    return prime_nums


def remove_multiple(prime, prime_numbers):
    for idx, val in enumerate(prime_numbers):
        if val % prime == 0:
            del prime_numbers[idx]
    return prime_numbers


def isWinner(x, nums):
    player_one_point = 0
    player_two_point = 0
    player_one_turns = True
    player_two_turns = False
    for n in nums:
        prime_nums = prime_numbers(n)
        if n == 1:
            prime_nums = [1]
        for index, prime in enumerate(prime_nums):
            if player_one_turns:
                player_one_point += 1
                player_one_turns = False
                player_two_turns = True
            elif player_two_turns:
                player_two_point += 1
                player_two_turns = False
                player_one_turns = True

            # prime_nums = remove_multiple(prime, prime_nums)

    if player_one_point > player_two_point:
        return 'Maria'
    elif player_two_point > player_one_point:
        return 'Ben'
    else:
        if player_one_turns:
            return 'Ben'
        elif player_two_turns:
            return 'Maria'


print((isWinner(3, [4, 5, 1])))

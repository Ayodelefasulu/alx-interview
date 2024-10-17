#!/usr/bin/python3
"""
Module to determine the winner of the prime game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime number game after x rounds.

    Args:
        x (int): The number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str: Name of the player who won the most rounds ("Maria" or "Ben").
             If there's no clear winner, return None.
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    # Count prime moves
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_moves[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

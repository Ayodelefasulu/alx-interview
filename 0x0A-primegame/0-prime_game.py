#!/usr/bin/python3
"""
This is the prime game module
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n, where n is the upper bound
            of consecutive integers for each round.

    Returns:
        str: The name of the player who won the most rounds,
            or None if the winner cannot be determined.
    """
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_primes(n):
        """Helper function to count the number of prime numbers up to n."""
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = count_primes(n)
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

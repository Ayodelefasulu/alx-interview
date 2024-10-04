#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    :param coins: A list of the coin denominations.
    :param total: The total amount of money we want to make change for.
    :return: The fewest number of coins needed to make change for total.
        Returns -1 if it is not possible.
    """
    if total <= 0:
        return 0

    # Initialize DP array with a high value (greater than any possible coin
    # count)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins needed to make total 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

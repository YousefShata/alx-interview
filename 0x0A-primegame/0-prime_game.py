#!/usr/bin/python3
"""
primegame module
"""


def isWinner(x, nums):
    """
    check who wins
    """
    def sieve_of_eratosthenes(max_n):
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        numbers = [True] * (n + 1)
        primes_left = [i for i in range(2, n + 1) if primes[i]]

        turn = 0

        while primes_left:
            prime = primes_left[0]
            primes_left = [p for p in primes_left if p % prime != 0]

            for i in range(prime, n + 1, prime):
                numbers[i] = False

            turn = 1 - turn  # Switch turns (0 -> 1 -> 0 ...)

        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

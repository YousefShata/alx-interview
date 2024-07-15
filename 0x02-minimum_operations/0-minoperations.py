#!/usr/bin/python3
"""
Mini calc
"""


def minOperations(n):
    """
    return minimum number or operatiosn to get to a number
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

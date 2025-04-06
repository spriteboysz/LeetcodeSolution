#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-06 16:19
FileName: algorithm/P1175. 质数排列.py
Description: 
"""
import math
from icecream import ic


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def sieve_of_eratosthenes(n):
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
            for p in range(2, int(n ** 0.5) + 1):
                if not primes[p]:
                    continue
                for multiple in range(p * p, n + 1, p):
                    primes[multiple] = False
            primes = [i for i, prime in enumerate(primes) if prime]
            return len(primes)

        m = sieve_of_eratosthenes(n)
        return (math.factorial(m) * math.factorial(n - m)) % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution().numPrimeArrangements(100)
    ic(solution)

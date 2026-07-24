#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-23 23:46
FileName: P0204. 计数质数.py
Description:
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, n):
            if not primes[i]:
                continue
            for j in range(i * i, n, i):
                primes[j] = False
        return len([prime for prime in primes if prime])


if __name__ == '__main__':
    solution = Solution().countPrimes(10)
    print(solution)

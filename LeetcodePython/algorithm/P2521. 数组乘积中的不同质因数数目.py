#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-11 22:48
FileName: algorithm/P2521. 数组乘积中的不同质因数数目.py
Description: 
"""
from functools import lru_cache, reduce
from typing import List

from icecream import ic


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = [True] * 1001
        for i in range(2, 1001):
            if not primes[i]:
                continue
            for j in range(i * 2, 1001, i):
                primes[j] = False
        primes = [i for i, v in enumerate(primes) if v][2:]

        @lru_cache
        def process(num):
            seen = set()
            for prime in primes:
                while num % prime == 0:
                    seen.add(prime)
                    num //= prime
                if num == 1:
                    break
            return seen

        seen2 = reduce(lambda s1, s2: s1 | s2, [process(num) for num in nums])
        return len(seen2)


if __name__ == '__main__':
    solution = Solution().distinctPrimeFactors(nums=[2, 4, 3, 7, 10, 6])
    ic(solution)

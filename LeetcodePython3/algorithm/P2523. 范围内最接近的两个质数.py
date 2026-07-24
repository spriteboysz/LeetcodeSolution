#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-24 00:00
FileName: P2523. 范围内最接近的两个质数.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        flags = [True] * (right + 1)
        flags[0] = flags[1] = False
        for i in range(right + 1):
            if not flags[i]:
                continue
            for j in range(i * i, right + 1, i):
                flags[j] = False
        primes = [i for i, flag in enumerate(flags) if flag and i >= left]
        if len(primes) < 2:
            return [-1, -1]
        minimum = min(num2 - num1 for num1, num2 in pairwise(primes))
        for num1, num2 in pairwise(primes):
            if num2 - num1 == minimum:
                return [num1, num2]
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().closestPrimes(10, 19)
    print(solution)

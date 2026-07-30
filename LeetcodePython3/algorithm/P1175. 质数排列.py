#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-29 22:01
FileName: P1175. 质数排列.py
Description:
"""
import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def calc(limit):
            flags = [True] * (limit + 1)
            flags[0], flags[1] = False, False
            for i in range(2, limit + 1):
                if not flags[i]:
                    continue
                for j in range(i * i, limit + 1, i):
                    flags[j] = False
            return sum(flags)

        cnt = calc(n)
        return math.factorial(cnt) * math.factorial(n - cnt) % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution().numPrimeArrangements(100)
    print(solution)

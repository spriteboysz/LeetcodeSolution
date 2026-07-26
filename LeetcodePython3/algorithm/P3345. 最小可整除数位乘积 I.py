#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 11:04
FileName: P3345. 最小可整除数位乘积 I.py
Description:
"""

from functools import reduce


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            s = reduce(lambda a, b: a * b, map(int, str(n)))
            if s % t == 0:
                return n
            n += 1


if __name__ == '__main__':
    solution = Solution().smallestNumber(n=15, t=3)
    print(solution)

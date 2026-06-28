#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 20:07
FileName: P3622. 判断整除性.py
Description:
"""
from functools import reduce


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(digit) for digit in str(n)]
        m = sum(digits) + reduce(lambda a, b: a * b, digits)
        return n % m == 0


if __name__ == '__main__':
    solution = Solution().checkDivisibility(99)
    print(solution)

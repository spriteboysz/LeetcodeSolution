#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 00:35
FileName: P1281. 整数的各位积和之差.py
Description:
"""
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        return reduce(lambda a, b: a * b, digits, 1) - sum(digits)


if __name__ == '__main__':
    solution = Solution().subtractProductAndSum(234)
    print(solution)

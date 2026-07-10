#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 23:43
FileName: P3658. 奇数和与偶数和的最大公约数.py
Description:
"""

import math


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return math.gcd(sum(range(0, n * 2, 2)), sum(range(1, n * 2, 2)))


if __name__ == '__main__':
    solution = Solution().gcdOfOddEvenSums(4)
    print(solution)

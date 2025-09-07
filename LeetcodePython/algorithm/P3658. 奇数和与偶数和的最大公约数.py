#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-09-07 22:20
FileName: P3658. 奇数和与偶数和的最大公约数.py
Description:
"""
from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = sum(i for i in range(n * 2 + 1) if i % 2 == 1)
        sum_even = sum(i for i in range(n * 2 + 1) if i % 2 == 0)
        return gcd(sum_odd, sum_even)


if __name__ == '__main__':
    s = Solution().gcdOfOddEvenSums(4)
    print(s)

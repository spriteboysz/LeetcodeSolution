#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-08-06 22:10
FileName: algorithm/P3622. 判断整除性.py
Description: 
"""
from functools import reduce
from icecream import ic


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nums = [int(d) for d in str(n)]
        m = reduce(lambda a, b: a + b, nums) + reduce(lambda a, b: a * b, nums)
        return n >= m and n % m == 0


if __name__ == '__main__':
    solution = Solution().checkDivisibility(8)
    ic(solution)

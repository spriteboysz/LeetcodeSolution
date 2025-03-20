#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-18 22:50
FileName: algorithm/P2614. 对角线上的质数.py
Description: 
"""
from functools import lru_cache
from typing import List

from icecream import ic


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        @lru_cache
        def check(num):
            if num <= 1:
                return False
            for d in range(2, int(num ** 0.5) + 1):
                if num % d == 0:
                    return False
            return True

        maximum = 0
        for i, row in enumerate(nums):
            if check(row[i]):
                maximum = max(maximum, row[i])
            if check(row[len(nums) - 1 - i]):
                maximum = max(maximum, row[len(nums) - 1 - i])
        return maximum


if __name__ == '__main__':
    solution = Solution().diagonalPrime(nums=[[1, 2, 3], [5, 6, 7], [9, 10, 11]])
    ic(solution)

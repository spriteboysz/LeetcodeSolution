#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-29 22:13
FileName: P3115. 质数的最大距离.py
Description:
"""
from functools import lru_cache
from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        @lru_cache
        def check(n):
            if n <= 1:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            return all(n % i != 0 for i in range(5, int(n ** 0.5) + 1, 2))

        indexes = [i for i, num in enumerate(nums) if check(num)]
        return indexes[-1] - indexes[0]


if __name__ == '__main__':
    solution = Solution().maximumPrimeDifference(nums=[4, 2, 9, 5, 3])
    print(solution)

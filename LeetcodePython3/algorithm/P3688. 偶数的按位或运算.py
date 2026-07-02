#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 23:27
FileName: P3688. 偶数的按位或运算.py
Description:
"""
from functools import reduce
from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        return reduce(
            lambda a, b: a | b,
            (num for num in nums if num % 2 == 0),
            0
        )


if __name__ == '__main__':
    solution = Solution().evenNumberBitwiseORs(nums=[1, 2, 3, 4, 5, 6])
    print(solution)

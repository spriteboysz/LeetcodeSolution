#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-06 22:46
FileName: algorithm/P3314. 构造最小位运算数组 I.py
Description: 
"""
from functools import lru_cache
from typing import List

from icecream import ic


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        @lru_cache
        def calc(n):
            if n == 2:
                return -1
            for i in range(1, n):
                if i | (i + 1) == n:
                    return i
            raise ValueError('Error')

        return [calc(num) for num in nums]


if __name__ == '__main__':
    solution = Solution().minBitwiseArray(nums=[2, 3, 5, 7])
    ic(solution)

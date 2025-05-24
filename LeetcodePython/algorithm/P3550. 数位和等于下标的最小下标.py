#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-24 10:02
FileName: algorithm/P3550. 数位和等于下标的最小下标.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(map(int, list(str(num)))) == i:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().smallestIndex(nums=[1, 10, 11])
    ic(solution)

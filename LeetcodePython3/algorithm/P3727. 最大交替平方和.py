#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-11 14:36
FileName: LC/P3727. 最大交替平方和.py
Description: 
"""
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs, reverse=True)
        total = 0
        for i, num in enumerate(nums):
            if i < len(nums) / 2:
                total += num ** 2
            else:
                total -= num ** 2
        return total


if __name__ == '__main__':
    solution = Solution().maxAlternatingSum([1, -1, 2, -2, 3, -3])
    print('<None>' if solution is None else f'{solution=}')

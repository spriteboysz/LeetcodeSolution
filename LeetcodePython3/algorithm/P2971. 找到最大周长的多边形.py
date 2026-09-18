#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 14:48
FileName: algorithm/P2971. 找到最大周长的多边形.py
Description: 
"""
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = sum(nums)
        for i, num in enumerate(nums[:-2]):
            total -= num
            if num < total:
                return num + total
        return -1


if __name__ == '__main__':
    solution = Solution().largestPerimeter(nums=[1, 12, 1, 2, 5, 50, 3])
    print('<None>' if solution is None else f'{solution=}')

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-24 23:02
FileName: algorithm/P2971. 找到最大周长的多边形.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ss = sum(nums)
        for num in nums:
            if num < ss - num:
                return ss
            ss -= num
        return -1


if __name__ == '__main__':
    solution = Solution().largestPerimeter(nums=[1, 12, 1, 2, 5, 50, 3])
    ic(solution)

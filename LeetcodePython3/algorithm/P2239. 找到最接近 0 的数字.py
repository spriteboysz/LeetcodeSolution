#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 16:48
FileName: P2239. 找到最接近 0 的数字.py
Description:
"""
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return sorted(nums, key=lambda num: (abs(num), -num))[0]


if __name__ == '__main__':
    solution = Solution().findClosestNumber(nums=[-4, -2,-1, 1, -1, 4, 8])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 13:44
FileName: P2441. 与对应负数同时存在的最大正整数.py
Description:
"""
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        seen = set(nums)
        for num in nums:
            if num < 0:
                break
            if num * -1 in seen:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().findMaxK(nums=[-1, 10, 6, 7, -7, 1])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-25 23:38
FileName: P1920. 基于排列构建数组.py
Description:
"""
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i, _ in enumerate(nums)]


if __name__ == '__main__':
    solution = Solution().buildArray(nums=[0, 2, 1, 5, 3, 4])
    print(solution)

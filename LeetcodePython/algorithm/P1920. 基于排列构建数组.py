#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-02 22:57
FileName: algorithm/P1920. 基于排列构建数组.py
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]


if __name__ == '__main__':
    solution = Solution().buildArray(nums=[0, 2, 1, 5, 3, 4])
    ic(solution)

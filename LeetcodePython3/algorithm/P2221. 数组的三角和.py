#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 22:35
FileName: P2221. 数组的三角和.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(num1 + num2) % 10 for num1, num2 in pairwise(nums)]
        return nums[0]


if __name__ == '__main__':
    solution = Solution().triangularSum(nums=[1, 2, 3, 4, 5])
    print(solution)

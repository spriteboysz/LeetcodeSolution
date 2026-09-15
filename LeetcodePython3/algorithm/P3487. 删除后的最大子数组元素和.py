#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 16:01
FileName: algorithm/P3487. 删除后的最大子数组元素和.py
Description: 
"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(num < 0 for num in nums):
            return max(nums)
        return sum(set(num for num in nums if num >= 0))


if __name__ == '__main__':
    solution = Solution().maxSum(nums=[1, 2, -1, -2, 1, 0, -1])
    print('<None>' if solution is None else f'{solution=}')

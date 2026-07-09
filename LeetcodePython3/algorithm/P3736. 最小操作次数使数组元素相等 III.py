#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 23:14
FileName: P3736. 最小操作次数使数组元素相等 III.py
Description:
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        return sum(maximum - num for num in nums)


if __name__ == '__main__':
    solution = Solution().minMoves(nums = [2,1,3])
    print(solution)

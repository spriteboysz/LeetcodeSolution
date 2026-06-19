#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 22:35
FileName: P0561. 数组拆分.py
Description:
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums, reverse=True)[1::2])


if __name__ == '__main__':
    solution = Solution().arrayPairSum([1, 3, 4, 2])
    print(solution)

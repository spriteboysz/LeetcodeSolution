#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:39
FileName: P2154. 将找到的值乘以 2.py
Description:
"""
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original


if __name__ == '__main__':
    solution = Solution().findFinalValue(nums=[5, 3, 6, 1, 12], original=3)
    print(solution)

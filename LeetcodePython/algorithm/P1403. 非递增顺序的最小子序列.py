#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 20:06
FileName: algorithm/P1403. 非递增顺序的最小子序列.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ss, acc = sum(nums), 0
        for i, num in enumerate(nums):
            acc += num
            if acc > ss - acc:
                return nums[:i + 1]
        return nums


if __name__ == '__main__':
    solution = Solution().minSubsequence(nums=[4, 4, 7, 6, 7])
    ic(solution)

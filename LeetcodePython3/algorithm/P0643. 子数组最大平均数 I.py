#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 11:57
FileName: P0643. 子数组最大平均数 I.py
Description:
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = curr = sum(nums[:k])
        for i, num in enumerate(nums[k:], start=k):
            curr = curr - nums[i - k] + num
            maximum = max(maximum, curr)
        return maximum / k


if __name__ == '__main__':
    solution = Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
    print(solution)

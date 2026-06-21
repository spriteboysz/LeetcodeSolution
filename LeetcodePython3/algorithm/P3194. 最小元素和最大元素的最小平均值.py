#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 15:25
FileName: P3194. 最小元素和最大元素的最小平均值.py
Description:
"""
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min(nums[i] + nums[-1 - i] for i in range(len(nums) // 2)) / 2


if __name__ == '__main__':
    solution = Solution().minimumAverage(nums=[7, 8, 3, 4, 15, 13, 4, 1])
    print(solution)

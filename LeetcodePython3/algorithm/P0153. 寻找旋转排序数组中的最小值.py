#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 20:28
FileName: P0153. 寻找旋转排序数组中的最小值.py
Description:
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]


if __name__ == '__main__':
    solution = Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2])
    print(solution)

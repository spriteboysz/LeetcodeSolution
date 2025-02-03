#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 10:26
FileName: P0704. 二分查找
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    solution = Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9)
    ic(solution)

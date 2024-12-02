#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 22:01
FileName: P0035. 搜索插入位置
Description:
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    solution = Solution().searchInsert(nums=[1, 3, 5, 6], target=5)
    print(solution)

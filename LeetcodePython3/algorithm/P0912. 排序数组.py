#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-23 23:23
FileName: P0912. 排序数组.py
Description:
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left = [num for num in nums if num < pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        return self.sortArray(left) + mid + self.sortArray(right)


if __name__ == '__main__':
    solution = Solution().sortArray([5, 2, 3, 1])
    print(solution)

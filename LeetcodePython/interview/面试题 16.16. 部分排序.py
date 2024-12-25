#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-24 23:08
FileName: 面试题 16.16. 部分排序
Description:
"""
from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        nums = sorted(array)
        if array == nums:
            return [-1, -1]
        left, right = -1, -1
        for i, num in enumerate(nums):
            if num != array[i]:
                left = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != array[j]:
                right = j
                break
        return [left, right]


if __name__ == '__main__':
    solution = Solution().subSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-26 18:40
FileName: P3912. 数组中的有效元素.py
Description:
"""


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        flags = [False] * n
        maximum = nums[0]
        for i, num in enumerate(nums):
            if i == 0 or i == len(nums) - 1:
                flags[i] = True
            elif num > maximum:
                flags[i] = True
                maximum = num
        maximum = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] > maximum:
                flags[i] = True
                maximum = nums[i]
        return [num for num, flag in zip(nums, flags) if flag]


if __name__ == '__main__':
    solution = Solution().findValidElements(nums=[1, 2, 4, 2, 3, 2])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 14:08
FileName: algorithm/P3912. 数组中的有效元素.py
Description: 
"""


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        flags = [False] * n
        maximum = 0
        for i, num in enumerate(nums):
            if num > maximum:
                flags[i] = True
                maximum = max(maximum, num)
        maximum = 0
        for i in range(n - 1, -1, -1):
            if nums[i] > maximum:
                flags[i] = True
                maximum = max(maximum, nums[i])

        return [num for num, flag in zip(nums, flags) if flag]


if __name__ == '__main__':
    solution = Solution().findValidElements([1, 2, 4, 2, 3, 2])
    print('<None>' if solution is None else f'{solution=}')

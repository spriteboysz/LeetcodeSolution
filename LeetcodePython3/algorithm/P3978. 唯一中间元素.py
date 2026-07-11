#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 23:14
FileName: P3978. 唯一中间元素.py
Description:
"""


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        return nums.count(nums[len(nums) // 2]) == 1


if __name__ == '__main__':
    solution = Solution().isMiddleElementUnique([1, 2, 3])
    print(solution)

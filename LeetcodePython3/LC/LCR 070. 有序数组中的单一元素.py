#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:30
FileName: 面试题/LCR 070. 有序数组中的单一元素.py
Description: 
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


if __name__ == '__main__':
    solution = Solution().singleNonDuplicate(nums=[3, 3, 7, 7, 10])
    print('<None>' if not solution else f'{solution=}')

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-22 23:04
FileName: P2717. 半有序排列.py
Description:
"""
from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        i1, i2 = nums.index(min(nums)), nums.index(max(nums))
        return i1 + len(nums) - 1 - i2 - int(i1 > i2)


if __name__ == '__main__':
    solution = Solution().semiOrderedPermutation([2, 1, 4, 3])
    print(solution)

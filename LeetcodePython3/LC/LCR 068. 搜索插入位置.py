#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 14:49
FileName: LC/LCR 068. 搜索插入位置.py
Description: 
"""
from bisect import bisect_left
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


if __name__ == '__main__':
    solution = Solution().searchInsert(nums=[1, 3, 5, 6], target=5)
    print('<None>' if not solution else f'{solution=}')

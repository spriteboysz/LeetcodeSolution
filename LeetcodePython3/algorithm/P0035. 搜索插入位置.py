#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 13:18
FileName: P0035. 搜索插入位置.py
Description:
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution().searchInsert(nums=[1, 3, 5, 6], target=10)
    print(solution)

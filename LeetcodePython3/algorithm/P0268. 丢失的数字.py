#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:12
FileName: P0268. 丢失的数字.py
Description:
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(len(nums)):
            if i not in seen:
                return i
        return len(nums)


if __name__ == '__main__':
    solution = Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(solution)

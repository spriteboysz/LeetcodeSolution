#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 17:10
FileName: P2057. 值相等的最小索引.py
Description:
"""
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().smallestEqual(nums = [0,1,2])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 09:14
FileName: algorithm/P3550. 数位和等于下标的最小下标.py
Description: 
"""
from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(int(c) for c in str(num)) == i:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().smallestIndex([1, 3, 2])
    print(solution)

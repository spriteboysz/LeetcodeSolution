#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:13
FileName: P0747. 至少是其他数字两倍的最大数.py
Description:
"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a, b, *_ = sorted(nums, reverse=True)
        return nums.index(a) if a >= b * 2 else -1


if __name__ == '__main__':
    solution = Solution().dominantIndex(nums=[3, 6, 1, 0])
    print(solution)

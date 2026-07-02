#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 22:53
FileName: P3769. 二进制反射排序.py
Description:
"""
from functools import lru_cache
from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        @lru_cache
        def calc(num):
            return int(bin(num)[2:][::-1]), num

        return sorted(nums, key=calc)


if __name__ == '__main__':
    solution = Solution().sortByReflection([8, 2])
    print(solution)

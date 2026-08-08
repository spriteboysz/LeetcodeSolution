#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-08 12:01
FileName: P1863. 找出所有子集的异或总和再求和.py
Description:
"""
from typing import List
from itertools import combinations
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for k in range(1, len(nums) + 1):
            for sub in combinations(nums, k):
                ans += reduce(lambda a, b: a ^ b, sub, initial=0)
        return ans


if __name__ == '__main__':
    solution = Solution().subsetXORSum(nums=[5, 1, 6])
    print(solution)

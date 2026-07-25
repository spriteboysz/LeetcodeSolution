#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-24 22:30
FileName: P0046. 全排列.py
Description:
"""
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums, r=len(nums))]


if __name__ == '__main__':
    solution = Solution().permute([1, 2, 3])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-24 22:33
FileName: P0047. 全排列 II.py
Description:
"""
from typing import List
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = {tuple(p) for p in permutations(nums, r=len(nums))}
        return [list(p) for p in seen]


if __name__ == '__main__':
    solution = Solution().permuteUnique([1,1,2])
    print(solution)

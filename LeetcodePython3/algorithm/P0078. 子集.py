#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 17:39
FileName: P0078. 子集.py
Description:
"""
from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        for k in range(len(nums) + 1):
            sets.extend([list(comb) for comb in combinations(nums, k)])
        return sets


if __name__ == '__main__':
    solution = Solution().subsets([1, 2, 3])
    print(solution)

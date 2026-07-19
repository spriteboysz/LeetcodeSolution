#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 17:43
FileName: P0090. 子集 II.py
Description:
"""
from itertools import combinations
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sets = set()
        for k in range(len(nums) + 1):
            for comb in combinations(nums, k):
                sets.add(tuple(sorted(list(comb))))
        return [list(s) for s in sets]


if __name__ == '__main__':
    solution = Solution().subsetsWithDup([1, 2, 2])
    print(solution)

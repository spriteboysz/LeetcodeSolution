#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-30 9:19
FileName: interview/面试题 08.04. 幂集.py
Description: 
"""
from typing import List
from itertools import combinations

from icecream import ic


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = []
        for n in range(len(nums) + 1):
            seen.extend([list(el) for el in combinations(nums, n)])
        return seen


if __name__ == '__main__':
    solution = Solution().subsets([1, 2, 3])
    ic(solution)

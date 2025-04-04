#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-30 16:05
FileName: LCR/LCR 084. 全排列 II.py
Description: 
"""
from typing import List
from itertools import permutations

from icecream import ic


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(el) for el in {el for el in permutations(nums)}]


if __name__ == '__main__':
    solution = Solution().permuteUnique([1, 1, 2])
    ic(solution)

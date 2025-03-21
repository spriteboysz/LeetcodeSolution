#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-21 22:06
FileName: algorithm/P0216. 组合总和 III.py
Description: 
"""
from typing import List
from itertools import combinations

from icecream import ic


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(comb) for comb in combinations([i + 1 for i in range(9)], k) if sum(comb) == n]


if __name__ == '__main__':
    solution = Solution().combinationSum3(3, 7)
    ic(solution)

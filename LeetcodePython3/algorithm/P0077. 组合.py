#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 17:36
FileName: P0077. 组合.py
Description:
"""
from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(comb) for comb in combinations(range(1, n + 1), k)]


if __name__ == '__main__':
    solution = Solution().combine(4, 2)
    print(solution)

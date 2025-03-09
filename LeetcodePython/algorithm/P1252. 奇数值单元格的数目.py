#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-09 15:36
FileName: algorithm/P1252. 奇数值单元格的数目.py
Description: 
"""
from typing import List
from collections import defaultdict

from icecream import ic


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, columns = defaultdict(int), defaultdict(int)
        for r, c in indices:
            rows[r] += 1
            columns[c] += 1
        return sum((rows[i] + columns[j]) % 2 for i in range(m) for j in range(n))


if __name__ == '__main__':
    solution = Solution().oddCells(m=2, n=3, indices=[[0, 1], [1, 1]])
    ic(solution)

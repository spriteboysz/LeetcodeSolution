#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 09:40
FileName: P1252. 奇数值单元格的数目.py
Description:
"""
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, columns = [False] * m, [False] * n
        for r, c in indices:
            rows[r] ^= 1
            columns[c] ^= 1
        a, b = sum(rows), sum(columns)
        return a * (n - b) + b * (m - a)


if __name__ == '__main__':
    solution = Solution().oddCells(m=2, n=3, indices=[[0, 1], [1, 1]])
    print(solution)

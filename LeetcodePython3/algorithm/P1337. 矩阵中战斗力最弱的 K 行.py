#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:44
FileName: P1337. 矩阵中战斗力最弱的 K 行.py
Description:
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = {i: sum(row) for i, row in enumerate(mat)}
        return sorted(rows, key=lambda k1: (rows[k1], k1))[:k]


if __name__ == '__main__':
    solution = Solution().kWeakestRows(
        mat=[[1, 1, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1]],
        k=3
    )
    print(solution)

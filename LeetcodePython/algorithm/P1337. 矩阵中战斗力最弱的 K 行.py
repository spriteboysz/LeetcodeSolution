#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 22:00
FileName: P1337. 矩阵中战斗力最弱的 K 行
Description:
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = [(sum(row), i) for i, row in enumerate(mat)]
        rows.sort()
        return [el[1] for el in rows[:k]]


if __name__ == '__main__':
    solution = Solution().kWeakestRows(
        mat=[[1, 1, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1]], k=3)
    print(solution)

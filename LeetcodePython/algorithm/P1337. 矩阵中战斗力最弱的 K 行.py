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
        rows = [(i, sum(row)) for i, row in enumerate(mat)]
        rows.sort(key=lambda el: (el[1], el[0]))
        return [el[0] for el in rows[:k]]


if __name__ == '__main__':
    solution = Solution().kWeakestRows(
        mat=[[1, 1, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1]], k=3)
    print(solution)

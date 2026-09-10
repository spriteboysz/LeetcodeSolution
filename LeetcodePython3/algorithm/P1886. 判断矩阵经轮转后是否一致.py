#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 16:49
FileName: algorithm/P1886. 判断矩阵经轮转后是否一致.py
Description: 
"""
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(grid):
            return [list(row)[::-1] for row in zip(*grid)]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False


if __name__ == '__main__':
    solution = Solution().findRotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]])
    print('<None>' if solution is None else f'{solution=}')

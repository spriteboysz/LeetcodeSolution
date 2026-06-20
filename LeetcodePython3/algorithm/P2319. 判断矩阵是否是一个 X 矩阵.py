#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:58
FileName: P2319. 判断矩阵是否是一个 X 矩阵.py
Description:
"""
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if i == j or i + j + 1 == len(grid):
                    if num == 0:
                        return False
                else:
                    if num != 0:
                        return False
        return True


if __name__ == '__main__':
    solution = Solution().checkXMatrix(grid=[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]])
    print(solution)

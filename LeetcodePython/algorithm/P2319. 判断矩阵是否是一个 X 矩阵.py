#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 23:20
FileName: P2319. 判断矩阵是否是一个 X 矩阵
Description:
"""
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or j == n - 1 - i:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True


if __name__ == '__main__':
    solution = Solution().checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]])
    print(solution)

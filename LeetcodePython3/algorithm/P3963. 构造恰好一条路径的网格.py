#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:45
FileName: P3963. 构造恰好一条路径的网格.py
Description:
"""


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        for j in range(n):
            grid[0][j] = '.'
        for i in range(m):
            grid[i][-1] = '.'
        return [''.join(row) for row in grid]


if __name__ == '__main__':
    solution = Solution().createGrid(4, 3)
    print(solution)

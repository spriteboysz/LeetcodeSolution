#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:45
FileName: LC/LCR 129. 字母迷宫.py
Description: 
"""
from typing import List


class Solution:
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
        def dfs(x, y, index):
            if not (0 <= x < n and 0 <= y < m) or target[index] != grid[x][y]:
                return False
            if index == len(target) - 1:
                return True

            grid[x][y] = '#'
            result = any(dfs(x + dx, y + dy, index + 1) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)])
            grid[x][y] = target[index]
            return result

        n, m = len(grid), len(grid[0])
        return any(dfs(i, j, 0) for i in range(n) for j in range(m))


if __name__ == '__main__':
    solution = Solution().wordPuzzle(
        grid=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        target="ABCCED"
    )
    print(solution)

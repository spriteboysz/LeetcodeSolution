#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-11 22:31
FileName: LCR/LCR 129. 字母迷宫.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
        def dfs(x, y, k):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != target[k]:
                return False
            if k == len(target) - 1:
                return True
            grid[x][y] = ''
            res = dfs(x + 1, y, k + 1) or dfs(x - 1, y, k + 1) or dfs(x, y + 1, k + 1) or dfs(x, y - 1, k + 1)
            grid[x][y] = target[k]
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().wordPuzzle(
        grid=[
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ],
        target="ABCCED")
    ic(solution)

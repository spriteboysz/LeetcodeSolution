#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-15 23:09
FileName: algorithm/P0130. 被围绕的区域.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = 'H'
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        for i in range(m):
            for j in range(n):
                if i != 0 and i != m - 1 and j != 0 and j != n - 1:
                    continue
                dfs(i, j)

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == 'O':
                    row[j] = 'X'
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == 'H':
                    row[j] = 'O'

        for row in board:
            ic(row)


if __name__ == '__main__':
    Solution().solve(board=[["X", "X", "X", "X"],
                            ["X", "O", "O", "X"],
                            ["X", "X", "O", "X"],
                            ["X", "O", "X", "X"]]
                     )

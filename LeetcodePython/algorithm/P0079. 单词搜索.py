#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-11 23:03
FileName: algorithm/P0079. 单词搜索.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])

        def dfs(x, y, k):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[x][y] = ''
            if any(dfs(x + dx, y + dy, k + 1) for dx, dy in directions):
                return True
            board[x][y] = word[k]
            return False

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))


if __name__ == '__main__':
    solution = Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED")
    ic(solution)

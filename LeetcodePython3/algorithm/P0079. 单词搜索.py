#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 18:39
FileName: algorithm/P0079. 单词搜索.py
Description: 
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, index: int):
            if x < 0 or x > n - 1 or y < 0 or y > m - 1:
                return False
            if board[x][y] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[x][y] = ''
            res = False
            for dx in [-1, 1]:
                res = res or dfs(x + dx, y, index + 1)
            for dy in [-1, 1]:
                res = res or dfs(x, y + dy, index + 1)
            board[x][y] = word[index]
            return res

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().exist(board=[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word="ABCCED")
    print(solution)

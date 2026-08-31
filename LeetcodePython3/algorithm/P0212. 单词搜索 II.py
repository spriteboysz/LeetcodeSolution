#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-19 23:06
FileName: algorithm/P0212. 单词搜索 II.py
Description: 
"""
from functools import lru_cache
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x: int, y: int, word: str, k: int):
            if not (0 <= x < n and 0 <= y < m) or board[x][y] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            board[x][y] = ''
            rs = any(dfs(x + dx, y + dy, word, k + 1) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)])
            board[x][y] = word[k]
            return rs

        @lru_cache
        def search(word):
            return any(dfs(i, j, word, 0) for i in range(n) for j in range(m))

        n, m = len(board), len(board[0])
        return sorted(word for word in words if search(word))


if __name__ == '__main__':
    solution = Solution().findWords(
        board=[["o", "a", "a", "n"],
               ["e", "t", "a", "e"],
               ["i", "h", "k", "r"],
               ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]
    )
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-24 22:48
FileName: P0419. 棋盘上的战舰.py
Description:
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == '.':
                    continue
                if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                    count += 1
        return count


if __name__ == '__main__':
    solution = Solution().countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]])
    print(solution)

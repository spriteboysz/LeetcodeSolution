#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 22:23
FileName: P0419. 棋盘上的战舰
Description:
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        for i, row in enumerate(board):
            for j, s in enumerate(row):
                if s == 'X' and (i == 0 or board[i - 1][j] != 'X') and (j == 0 or board[i][j - 1] != 'X'):
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]])
    print(solution)

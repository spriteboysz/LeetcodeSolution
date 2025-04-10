#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-08 23:48
FileName: interview/面试题 16.04. 井字游戏.py
Description: 
"""
from typing import List
from collections import Counter

from icecream import ic


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        def check(position):
            if not position:
                return False
            if max(Counter([x for x, _ in position]).values()) == n:
                return True
            if max(Counter([y for _, y in position]).values()) == n:
                return True
            if all((x, x) in position for x in range(n)):
                return True
            if all((x, n - 1 - x) in position for x in range(n)):
                return True
            return False

        position1, position2, n = [], [], len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'O':
                    position1.append((i, j))
                if board[i][j] == 'X':
                    position2.append((i, j))

        if check(position1):
            return 'O'
        if check(position2):
            return 'X'
        return 'Draw' if ' ' not in ''.join(board) else 'Pending'


if __name__ == '__main__':
    solution = Solution().tictactoe(board=["O X", " XO", "X O"])
    ic(solution)

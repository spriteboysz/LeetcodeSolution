#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 21:51
FileName: algorithm/P1275. 找出井字棋的获胜者.py
Description: 
"""
from typing import List
from collections import Counter

from icecream import ic


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check(grid):
            if not grid:
                return False
            if max(Counter(el[0] for el in grid).values()) >= 3:
                return True
            if max(Counter(el[1] for el in grid).values()) >= 3:
                return True
            if [0, 0] in grid and [1, 1] in grid and [2, 2] in grid:
                return True
            if [0, 2] in grid and [1, 1] in grid and [2, 0] in grid:
                return True
            return False

        if check(moves[::2]):
            return 'A'
        if check(moves[1::2]):
            return 'B'
        return 'Pending' if len(moves) < 9 else 'Draw'


if __name__ == '__main__':
    solution = Solution().tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 12:27
FileName: algorithm/P1275. 找出井字棋的获胜者.py
Description: 
"""
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check(grid):
            results = [[grid[0][0], grid[1][1], grid[2][2]], [grid[0][2], grid[1][1], grid[2][0]]]
            for row in grid:
                results.append(row)
            for col in zip(*grid):
                results.append(list(col))
            for result in results:
                if '.' not in result and len(set(result)) == 1:
                    return result[0]
            return 'Pending' if '.' in sum(grid, []) else 'Draw'

        board = [['.' for _ in range(3)] for _ in range(3)]
        for i, move in enumerate(moves):
            x, y = move
            if i % 2 == 0:
                board[x][y] = 'A'
            else:
                board[x][y] = 'B'
        return check(board)


if __name__ == '__main__':
    solution = Solution().tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]])
    print('<None>' if solution is None else f'{solution=}')

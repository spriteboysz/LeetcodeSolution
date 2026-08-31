#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-31 21:58
FileName: algorithm/P0037. 解数独.py
Description: 
"""
from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(k: int) -> bool:
            if k == len(unfilled):
                return True

            x, y = unfilled[k]
            b = x // 3 * 3 + y // 3
            for v in cols[y] & blks[b] & rows[x]:
                rows[x].remove(v)
                cols[y].remove(v)
                blks[b].remove(v)
                board[x][y] = str(v)
                if backtrack(k + 1):
                    return True
                rows[x].add(v)
                cols[y].add(v)
                blks[b].add(v)
            return False

        rows: List[Set[int]] = [set(range(1, 10)) for _ in range(9)]
        cols: List[Set[int]] = [set(range(1, 10)) for _ in range(9)]
        blks: List[Set[int]] = [set(range(1, 10)) for _ in range(9)]

        unfilled = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    unfilled.append((i, j))
                else:
                    rows[i].discard(int(board[i][j]))
                    cols[j].discard(int(board[i][j]))
                    blks[i // 3 * 3 + j // 3].discard(int(board[i][j]))

        backtrack(0)

        for row in board:
            print(' '.join(map(str, row)))


if __name__ == '__main__':
    Solution().solveSudoku(
        [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    )

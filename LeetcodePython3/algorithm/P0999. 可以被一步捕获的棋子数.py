#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-27 22:30
FileName: P0999. 可以被一步捕获的棋子数.py
Description:
"""
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def calc(rows):
            rows = [''.join(el for el in row if el != '.') for row in rows]
            return sum(row.count('pR') + row.count('Rp') for row in rows)

        return calc([row for row in board if 'R' in row]) + calc([column for column in zip(*board) if 'R' in column])


if __name__ == '__main__':
    solution = Solution().numRookCaptures(
        [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]
    )
    print(solution)

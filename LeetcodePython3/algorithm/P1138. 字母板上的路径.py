#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 09:54
FileName: algorithm/P1138. 字母板上的路径.py
Description: 
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        x1, y1 = 0, 0
        moves = []
        for ch in target:
            x2, y2 = divmod(ord(ch) - ord('a'), 5)
            if x2 < x1:
                moves.append('U' * (x1 - x2))
            if y2 < y1:
                moves.append('L' * (y1 - y2))
            if x2 > x1:
                moves.append('D' * (x2 - x1))
            if y2 > y1:
                moves.append('R' * (y2 - y1))
            moves.append('!')
            x1, y1 = x2, y2
        return ''.join(moves)


if __name__ == '__main__':
    solution = Solution().alphabetBoardPath(target="leet")
    print(solution)

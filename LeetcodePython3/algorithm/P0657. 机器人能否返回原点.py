#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:40
FileName: P0657. 机器人能否返回原点.py
Description:
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


if __name__ == '__main__':
    solution = Solution().judgeCircle(moves="UD")
    print(solution)

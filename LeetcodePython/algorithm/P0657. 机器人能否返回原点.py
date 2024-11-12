#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-12 23:11
FileName: P0657. 机器人能否返回原点
Description:
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


if __name__ == '__main__':
    solution = Solution().judgeCircle('UD')
    print(solution)

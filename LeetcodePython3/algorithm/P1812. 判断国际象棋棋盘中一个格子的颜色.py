#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:04
FileName: P1812. 判断国际象棋棋盘中一个格子的颜色.py
Description:
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) + int(coordinates[1])) % 2 == 1


if __name__ == '__main__':
    solution = Solution().squareIsWhite('a1')
    print(solution)

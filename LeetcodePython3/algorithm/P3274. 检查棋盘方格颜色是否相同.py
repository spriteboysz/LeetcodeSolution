#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:11
FileName: P3274. 检查棋盘方格颜色是否相同.py
Description:
"""


class Solution:
    @staticmethod
    def calc(coordinate):
        return ord(coordinate[0]) + int(coordinate[1])

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return self.calc(coordinate1) % 2 == self.calc(coordinate2) % 2


if __name__ == '__main__':
    solution = Solution().checkTwoChessboards('a1', 'c3')
    print(solution)

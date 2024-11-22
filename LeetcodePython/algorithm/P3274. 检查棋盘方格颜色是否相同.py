#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-21 22:59
FileName: P3274. 检查棋盘方格颜色是否相同
Description:
"""


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        num1, num2 = map(lambda el: (ord(el[0]) + ord(el[1])) % 2 == 0, [coordinate1, coordinate2])
        return num1 == num2


if __name__ == '__main__':
    solution = Solution().checkTwoChessboards('a1', 'c3')
    print(solution)

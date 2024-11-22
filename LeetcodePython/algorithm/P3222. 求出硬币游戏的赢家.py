#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 22:07
FileName: P3222. 求出硬币游戏的赢家
Description:
"""


class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if min(x, y // 4) % 2 == 0:
            return 'Bob'
        return 'Alice'


if __name__ == '__main__':
    solution = Solution().winningPlayer(4, 11)
    print(solution)

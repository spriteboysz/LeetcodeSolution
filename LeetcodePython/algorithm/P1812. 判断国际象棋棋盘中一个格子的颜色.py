#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 21:17
FileName: P1812. 判断国际象棋棋盘中一个格子的颜色
Description:
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return sum(map(ord, coordinates)) % 2 == 1


if __name__ == '__main__':
    solution = Solution().squareIsWhite('a1')
    print(solution)

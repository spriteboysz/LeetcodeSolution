#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-13 19:14
FileName: algorithm/P3537. 填充特殊网格.py
Description: 
"""

from icecream import ic


class Solution:
    def specialGrid(self, n: int) -> list[list[int]]:
        m = 2 ** n
        grid = [[0] * m for _ in range(m)]
        matches = [
            lambda x, y, offset: (x, y + offset),
            lambda x, y, offset: (x + offset, y + offset),
            lambda x, y, offset: (x + offset, y),
            lambda x, y, offset: (x, y)
        ]
        for i in range(m * m):
            dx, dy = 0, 0
            for j in range(n):
                half = 2 ** j
                dx, dy = matches[(i >> (2 * j)) & 3](dx, dy, half)
                grid[dx][dy] = i
        return grid


if __name__ == '__main__':
    solution = Solution().specialGrid(3)
    ic(solution)

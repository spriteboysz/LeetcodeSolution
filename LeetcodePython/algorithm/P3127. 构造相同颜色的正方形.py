#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 23:02
FileName: P3127. 构造相同颜色的正方形
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        grid1 = [grid[0][0], grid[0][1], grid[1][0], grid[1][1]]
        grid2 = [grid[0][1], grid[0][2], grid[1][1], grid[1][2]]
        grid3 = [grid[1][0], grid[1][1], grid[2][0], grid[2][1]]
        grid4 = [grid[1][1], grid[1][2], grid[2][1], grid[2][2]]

        for g in [grid1, grid2, grid3, grid4]:
            if g.count('B') != 2:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]])
    ic(solution)

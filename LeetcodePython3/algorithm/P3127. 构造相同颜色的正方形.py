#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:07
FileName: P3127. 构造相同颜色的正方形.py
Description:
"""
from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i, row in enumerate(grid[1:], start=1):
            for j, _ in enumerate(row[1:], start=1):
                block = [grid[i - 1][j - 1], grid[i][j - 1], grid[i - 1][j], grid[i][j]]
                if block.count('B') <= 1 or block.count('W') <= 1:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().canMakeSquare(grid=[["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-25 22:41
FileName: algorithm/P1861. 旋转盒子.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        grid = [''.join(row) for row in boxGrid]
        for j, row in enumerate(grid):
            sub_rows = row.split('*')
            for i, sub in enumerate(sub_rows):
                sub_rows[i] = ''.join(sorted(sub, reverse=True))
            grid[j] = '*'.join(sub_rows)
        grid2 = [[''] * len(grid) for _ in range(len(grid[0]))]
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                grid2[j][len(grid) - 1 - i] = el
        return grid2


if __name__ == '__main__':
    solution = Solution().rotateTheBox(
        [["#", "#", "*", ".", "*", "."],
         ["#", "#", "#", "*", ".", "."],
         ["#", "#", "#", ".", "#", "."]])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-06 23:21
FileName: LCR/P3417. 跳过交替单元格的之字形遍历.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        for i, row in enumerate(grid):
            if i % 2 == 1:
                row.reverse()
        return sum(grid, [])[::2]


if __name__ == '__main__':
    solution = Solution().zigzagTraversal(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 16:15
FileName: algorithm/P3417. 跳过交替单元格的之字形遍历.py
Description: 
"""
from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        nums = []
        for i, row in enumerate(grid):
            if i % 2 == 0:
                nums.extend(row[::2])
            else:
                nums.extend(row[1::2][::-1])
        return nums


if __name__ == '__main__':
    solution = Solution().zigzagTraversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('<None>' if solution is None else f'{solution=}')

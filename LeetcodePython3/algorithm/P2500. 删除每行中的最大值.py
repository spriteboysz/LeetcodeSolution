#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 16:35
FileName: P2500. 删除每行中的最大值.py
Description:
"""
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        return sum(max(column) for column in zip(*grid))


if __name__ == '__main__':
    solution = Solution().deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]])
    print(solution)

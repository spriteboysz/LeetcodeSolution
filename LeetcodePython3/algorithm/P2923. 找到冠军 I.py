#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 21:35
FileName: P2923. 找到冠军 I.py
Description:
"""
from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            if sum(row) == len(grid) - 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findChampion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]])
    print(solution)

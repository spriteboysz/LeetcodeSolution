#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 22:01
FileName: P2923. 找到冠军 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            if sum(row) == len(row) - 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findChampion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]])
    ic(solution)

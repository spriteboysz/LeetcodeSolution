#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-22 22:46
FileName: P3142. 判断矩阵是否满足条件.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        if len(set(tuple(row) for row in grid)) != 1:
            return False
        return all(num1 != num2 for num1, num2 in pairwise(grid[0]))


if __name__ == '__main__':
    solution = Solution().satisfiesConditions(grid=[[1, 0, 2], [1, 0, 2]])
    print(solution)

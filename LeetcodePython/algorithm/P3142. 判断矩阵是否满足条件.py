#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 22:51
FileName: P3142. 判断矩阵是否满足条件
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(1, len(grid[0])):
            if grid[0][i - 1] == grid[0][i]:
                return False
        return len(set(tuple(row) for row in grid)) == 1


if __name__ == '__main__':
    solution = Solution().satisfiesConditions(grid=[[1, 0, 2], [1, 0, 2]])
    ic(solution)

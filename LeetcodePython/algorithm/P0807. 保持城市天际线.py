#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 22:08
FileName: P0807. 保持城市天际线
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows, columns = [0] * n, [0] * n
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                rows[i] = max(rows[i], num)
                columns[j] = max(columns[j], num)
        cnt = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                cnt += min(rows[i], columns[j]) - num
        return cnt


if __name__ == '__main__':
    solution = Solution().maxIncreaseKeepingSkyline(grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
    ic(solution)

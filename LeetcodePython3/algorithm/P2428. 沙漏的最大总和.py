#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-11 22:38
FileName: P2428. 沙漏的最大总和.py
Description:
"""
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum = 0
        n, m = len(grid), len(grid[0])
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                maximum = max(maximum, sum(grid[i - 1][j - 1:j + 2]) + sum(grid[i + 1][j - 1:j + 2]) + grid[i][j])
        return maximum


if __name__ == '__main__':
    solution = Solution().maxSum([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]])
    print(solution)

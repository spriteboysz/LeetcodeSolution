#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-20 23:08
FileName: P2428. 沙漏的最大总和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                maximum = max(maximum, sum(grid[i][j:j + 3]) + grid[i + 1][j + 1] + sum(grid[i + 2][j:j + 3]))
        return maximum


if __name__ == '__main__':
    solution = Solution().maxSum(grid=[[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]])
    ic(solution)

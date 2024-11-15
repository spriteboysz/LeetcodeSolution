#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 21:50
FileName: P1351. 统计有序矩阵中的负数
Description:
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for row in grid:
            for num in row:
                if num < 0:
                    cnt += 1
        return sum([int(num < 0) for row in grid for num in row])


if __name__ == '__main__':
    solution = Solution().countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
    print(solution)

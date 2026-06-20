#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:17
FileName: P1351. 统计有序矩阵中的负数.py
Description:
"""
import numpy as np

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        arr = np.array(grid)
        return np.size(arr[arr < 0])


if __name__ == '__main__':
    solution = Solution().countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
    print(solution)

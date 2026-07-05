#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 13:31
FileName: P0074. 搜索二维矩阵.py
Description:
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, row in enumerate(matrix):
            if target > row[-1]:
                continue
            for j, num in enumerate(row):
                if num == target:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
    print(solution)

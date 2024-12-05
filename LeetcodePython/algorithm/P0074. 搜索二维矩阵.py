#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-04 22:15
FileName: P0074. 搜索二维矩阵
Description:
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in set(row):
                return True
        return False


if __name__ == '__main__':
    solution = Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
    print(solution)

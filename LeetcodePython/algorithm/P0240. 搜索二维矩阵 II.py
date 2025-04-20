#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 20:44
FileName: algorithm/P0240. 搜索二维矩阵 II.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            if row[0] > target:
                return False
            else:
                if target in row:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().searchMatrix(
        matrix=[[1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]],
        target=5)
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 08:59
FileName: 面试题/面试题 10.09. 排序矩阵查找.py
Description: 
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if not row:
                return False
            left, right = row[0], row[-1]
            if left <= target <= right:
                if target in row:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().searchMatrix(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        target=5
    )
    print('<None>' if not solution else f'{solution=}')

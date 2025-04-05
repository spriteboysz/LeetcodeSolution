#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 11:08
FileName: algorithm/P0059. 螺旋矩阵 II.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[n * n]]
        num = n * n
        while num > 1:
            matrix = [list(row)[::-1] for row in zip(*matrix)]
            m = len(matrix[0])
            matrix = [list(range(num - m, num)), *matrix]
            num -= m
        return matrix


if __name__ == '__main__':
    solution = Solution().generateMatrix(4)
    ic(solution)

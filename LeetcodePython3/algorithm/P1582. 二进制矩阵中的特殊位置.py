#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 21:19
FileName: P1582. 二进制矩阵中的特殊位置.py
Description:
"""
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        columns = [sum(column) for column in zip(*mat)]
        return sum(num == 1 and rows[i] == 1 and columns[j] == 1
                   for i, row in enumerate(mat) for j, num in enumerate(row))


if __name__ == '__main__':
    solution = Solution().numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(solution)

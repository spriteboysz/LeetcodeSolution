#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 23:12
FileName: P1582. 二进制矩阵中的特殊位置
Description:
"""
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        columns = [sum(column) for column in zip(*mat)]
        cnt, n, m = 0, len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rows[i] == 1 and columns[j] == 1:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]])
    print(solution)

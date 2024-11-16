#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 11:44
FileName: P3033. 修改矩阵
Description:
"""
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        columns = [max(row) for row in zip(*matrix)]
        for row in matrix:
            for j, num in enumerate(row):
                if num == -1:
                    row[j] = columns[j]
        return matrix


if __name__ == '__main__':
    solution = Solution().modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]])
    print(solution)

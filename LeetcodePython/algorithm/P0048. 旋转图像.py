#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-03 23:12
FileName: P0048. 旋转图像
Description:
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(0, len(matrix)):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)


if __name__ == '__main__':
    Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

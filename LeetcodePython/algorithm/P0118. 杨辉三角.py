#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-02 22:30
FileName: P0118. 杨辉三角
Description:
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(numRows - 1):
            row = triangle[-1]
            row = [1, *[num1 + num2 for num1, num2 in zip(row, row[1:])], 1]
            triangle.append(row.copy())

        return triangle[:numRows]


if __name__ == '__main__':
    solution = Solution().generate(5)
    print(solution)

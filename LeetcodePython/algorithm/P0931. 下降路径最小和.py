#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 22:11
FileName: algorithm/P0931. 下降路径最小和.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                nums = [matrix[i - 1][j]]
                if j - 1 >= 0:
                    nums.append(matrix[i - 1][j - 1])
                if j + 1 < len(matrix[0]):
                    nums.append(matrix[i - 1][j + 1])
                matrix[i][j] += min(nums)
        return min(matrix[-1])


if __name__ == '__main__':
    solution = Solution().minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]])
    ic(solution)

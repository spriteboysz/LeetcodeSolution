#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 21:15
FileName: P0566. 重塑矩阵
Description:
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        nums = [mat[i][j] for i in range(m) for j in range(n)]
        return [nums[i * c:i * c + c] for i in range(r)]


if __name__ == '__main__':
    solution = Solution().matrixReshape(mat=[[1, 2, 3, 4]], r=4, c=1)
    print(solution)

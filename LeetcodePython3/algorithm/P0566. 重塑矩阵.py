#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 18:37
FileName: P0566. 重塑矩阵.py
Description:
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        nums = sum(mat, [])
        return [nums[i:i + c] for i in range(0, len(nums), c)]



if __name__ == '__main__':
    solution = Solution().matrixReshape(mat=[[1, 2, 3], [4, 5, 6]], r=3, c=2)
    print(solution)

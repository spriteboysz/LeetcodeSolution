#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 10:46
FileName: P1886. 判断矩阵经轮转后是否一致
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        def process(grid):
            return [list(el) for el in zip(*grid)][::-1]

        for _ in range(3):
            mat = process(mat)
            ic(mat)
            if mat == target:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().findRotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]])
    ic(solution)

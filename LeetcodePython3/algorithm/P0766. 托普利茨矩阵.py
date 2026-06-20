#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 22:47
FileName: P0766. 托普利茨矩阵.py
Description:
"""
from collections import defaultdict

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic = defaultdict(set)
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                dic[i - j].add(num)
                if len(dic[i - j]) > 1:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution().isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
                                           )
    print(solution)

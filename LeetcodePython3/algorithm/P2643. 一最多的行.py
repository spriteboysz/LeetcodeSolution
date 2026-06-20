#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 13:32
FileName: P2643. 一最多的行.py
Description:
"""
from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows = [sum(row) for row in mat]
        maximum = max(rows)
        for i, row in enumerate(rows):
            if row == maximum:
                return [i, row]
        raise ValueError('Error')

if __name__ == '__main__':
    solution = Solution().rowAndMaximumOnes(mat=[[0, 1], [1, 0]])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 16:09
FileName: algorithm/P2946. 循环移位后的矩阵相似检查.py
Description: 
"""
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n, m = len(mat), len(mat[0])
        k %= m
        if k == 0:
            return True
        for i, row in enumerate(mat):
            if i % 2 == 0:
                if row != row[k:] + row[:k]:
                    return False
            else:
                if row != row[-k:] + row[:-k]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution().areSimilar(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=4)
    print('<None>' if solution is None else f'{solution=}')

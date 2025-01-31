#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 22:23
FileName: P2946. 循环移位后的矩阵相似检查
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        for i, row in enumerate(mat):
            if i % 2 == 0:
                if row != row[k:] + row[:k]:
                    return False
            else:
                if row != row[-k:] + row[:-k]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution().areSimilar(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2)
    ic(solution)

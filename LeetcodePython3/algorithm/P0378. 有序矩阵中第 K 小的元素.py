#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 22:53
FileName: P0378. 有序矩阵中第 K 小的元素.py
Description:
"""
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(sum(matrix, []))[k - 1]


if __name__ == '__main__':
    solution = Solution().kthSmallest([[1,2],[1,3]], 2)
    print(solution)

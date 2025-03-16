#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 23:08
FileName: algorithm/P0378. 有序矩阵中第 K 小的元素.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([num for row in matrix for num in row])[k - 1]


if __name__ == '__main__':
    solution = Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8)
    ic(solution)

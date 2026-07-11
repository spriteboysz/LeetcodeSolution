#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 11:15
FileName: P2679. 矩阵中的和.py
Description:
"""
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for num in nums:
            num.sort(reverse=True)
        return sum(max(list(column)) for column in zip(*nums))


if __name__ == '__main__':
    solution = Solution().matrixSum(nums=[[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]])
    print(solution)

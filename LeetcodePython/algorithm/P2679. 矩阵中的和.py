#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-17 22:53
FileName: P2679. 矩阵中的和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        return sum(max(column) for column in zip(*nums))


if __name__ == '__main__':
    solution = Solution().matrixSum(nums=[[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]])
    ic(solution)

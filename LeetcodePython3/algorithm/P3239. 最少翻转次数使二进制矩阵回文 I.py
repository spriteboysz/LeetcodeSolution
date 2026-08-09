#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 09:55
FileName: P3239. 最少翻转次数使二进制矩阵回文 I.py
Description:
"""
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def calc_row(nums: List[int]) -> int:
            return sum(nums[i] != nums[-1 - i] for i in range(len(nums) // 2))

        def calc(matrix) -> int:
            return sum(calc_row(row) for row in matrix)

        return min(calc(grid), calc(zip(*grid)))


if __name__ == '__main__':
    solution = Solution().minFlips(grid=[[0, 1], [0, 1], [0, 0]])
    print(solution)

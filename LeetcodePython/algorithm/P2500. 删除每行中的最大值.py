#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 11:10
FileName: P2500. 删除每行中的最大值
Description:
"""
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            row.sort()
        return sum([max(row) for row in zip(*grid)])


if __name__ == '__main__':
    solution = Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 11:24
FileName: P2639. 查询网格图中每一列的宽度
Description:
"""
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(num)) for num in row) for row in zip(*grid)]


if __name__ == '__main__':
    solution = Solution().findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]])
    print(solution)

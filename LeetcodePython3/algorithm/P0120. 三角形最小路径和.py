#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-17 23:01
FileName: algorithm/P0120. 三角形最小路径和.py
Description: 
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i, row in enumerate(triangle):
            for j, v in enumerate(row):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(row) - 1:
                    triangle[i][j] += triangle[i - 1][-1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])


if __name__ == '__main__':
    solution = Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(solution)

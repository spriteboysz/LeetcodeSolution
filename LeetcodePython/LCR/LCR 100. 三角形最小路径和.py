#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 22:55
FileName: LCR/LCR 100. 三角形最小路径和.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])


if __name__ == '__main__':
    solution = Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 21:24
FileName: P1051. 高度检查器.py
Description:
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


if __name__ == '__main__':
    solution = Solution().heightChecker(heights=[1, 1, 4, 2, 1, 3])
    print(solution)

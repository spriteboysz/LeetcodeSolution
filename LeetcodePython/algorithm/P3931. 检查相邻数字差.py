#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-05-17 19:12
FileName: P3931. 检查相邻数字差.py
Description:
"""
from itertools import pairwise


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(abs(int(a) - int(b)) <= 2 for a, b in pairwise(s))


if __name__ == '__main__':
    solution = Solution().isAdjacentDiffAtMostTwo('132456')
    print(solution)

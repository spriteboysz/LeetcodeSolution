#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 09:01
FileName: P3931. 检查相邻数字差.py
Description:
"""
from itertools import pairwise


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(abs(int(ch1) - int(ch2)) <= 2 for ch1, ch2 in pairwise(s))


if __name__ == '__main__':
    solution = Solution().isAdjacentDiffAtMostTwo(s="132")
    print(solution)

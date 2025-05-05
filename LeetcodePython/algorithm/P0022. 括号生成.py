#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-05 18:17
FileName: algorithm/P0022. 括号生成.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths, path = [], []

        def backtrace(m, l):
            if m == 2 * n:
                paths.append("".join(path))
            if l < n:
                path.append("(")
                backtrace(m + 1, l + 1)
                path.pop()
            if m - l < l:
                path.append(")")
                backtrace(m + 1, l)
                path.pop()

        backtrace(0, 0)
        return paths


if __name__ == '__main__':
    solution = Solution().generateParenthesis(3)
    ic(solution)

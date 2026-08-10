#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 22:43
FileName: P0022. 括号生成.py
Description:
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths, path = [], []

        def backtrace(left: int, right: int) -> None:
            if len(path) == n * 2:
                paths.append(''.join(path))
                return
            if left < n:
                path.append('(')
                backtrace(left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                backtrace(left, right + 1)
                path.pop()

        backtrace(0, 0)
        return paths


if __name__ == '__main__':
    solution = Solution().generateParenthesis(4)
    print(solution)

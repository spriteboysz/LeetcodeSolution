#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:44
FileName: P0397. 整数替换.py
Description:
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))


if __name__ == '__main__':
    solution = Solution().integerReplacement(10)
    print(solution)

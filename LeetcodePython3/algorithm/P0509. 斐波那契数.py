#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 11:51
FileName: P0509. 斐波那契数.py
Description:
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    solution = Solution().fib(2)
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 14:41
FileName: LC/LCR 126. 斐波那契数.py
Description: 
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution().fib(100)
    print(solution)

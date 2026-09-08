#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 08:53
FileName: 面试题/面试题 08.01. 三步问题.py
Description: 
"""


class Solution:
    def waysToStep(self, n: int) -> int:
        a, b, c = 4, 2, 1
        if n < 3:
            return n
        if n == 3:
            return 4
        for _ in range(n - 3):
            a, b, c = (a + b + c) % 1000000007, a, b
        return a


if __name__ == '__main__':
    solution = Solution().waysToStep(10)
    print('<None>' if not solution else f'{solution=}')

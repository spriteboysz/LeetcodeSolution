#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 09:31
FileName: P1137. 第 N 个泰波那契数.py
Description:
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        for _ in range(n - 2):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2 if n > 0 else t0


if __name__ == '__main__':
    solution = Solution().tribonacci(25)
    print(solution)

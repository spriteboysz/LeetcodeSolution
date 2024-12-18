#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-18 23:46
FileName: P1137. 第 N 个泰波那契数
Description:
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return min(n, 1)
        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c


if __name__ == '__main__':
    solution = Solution().tribonacci(25)
    print(solution)

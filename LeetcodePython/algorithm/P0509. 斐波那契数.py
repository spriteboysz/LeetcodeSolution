#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 18:33
FileName: P0509. 斐波那契数
Description:
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    solution = Solution().fib(2)
    print(solution)

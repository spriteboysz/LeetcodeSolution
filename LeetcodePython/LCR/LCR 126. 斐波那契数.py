#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:23
FileName: LCR 126. 斐波那契数
Description:
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution().fib(4)
    print(solution)

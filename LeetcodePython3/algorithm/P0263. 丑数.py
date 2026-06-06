#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:08
FileName: P0263. 丑数.py
Description:
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        for factor in [2, 3, 5]:
            while n and n % factor == 0:
                n //= factor
        return n == 1


if __name__ == '__main__':
    solution = Solution().isUgly(6)
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 11:29
FileName: 面试题/面试题 08.05. 递归乘法.py
Description: 
"""


class Solution:
    def multiply(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        minimum, maximum = min(a, b), max(a, b)
        return sum(maximum for _ in range(minimum))


if __name__ == '__main__':
    solution = Solution()
    print(solution)

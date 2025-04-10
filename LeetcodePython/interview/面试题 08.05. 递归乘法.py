#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-08 23:44
FileName: interview/面试题 08.05. 递归乘法.py
Description: 
"""

from icecream import ic


class Solution:
    def multiply(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        minimum, maximum = min(a, b), max(a, b)
        return sum(maximum for _ in range(minimum))


if __name__ == '__main__':
    solution = Solution().multiply(2, 6)
    ic(solution)

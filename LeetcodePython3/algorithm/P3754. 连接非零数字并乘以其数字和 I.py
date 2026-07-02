#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 22:50
FileName: P3754. 连接非零数字并乘以其数字和 I.py
Description:
"""


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ''.join(digit for digit in str(n) if digit != '0')
        if not s:
            return 0
        return int(s) * sum(map(int, list(s)))


if __name__ == '__main__':
    solution = Solution().sumAndMultiply(n = 10203004)
    print(solution)

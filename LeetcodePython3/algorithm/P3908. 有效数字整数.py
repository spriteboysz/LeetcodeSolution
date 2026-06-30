#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:32
FileName: P3908. 有效数字整数.py
Description:
"""


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(x) in str(n) and not str(n).startswith(str(x))


if __name__ == '__main__':
    solution = Solution().validDigit(101, 0)
    print(solution)

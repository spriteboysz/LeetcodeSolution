#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:01
FileName: P1374. 生成每种字符都是奇数个的字符串.py
Description:
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        return 'x' * (n - 1) + 'y' if n % 2 == 0 else 'x' * n


if __name__ == '__main__':
    solution = Solution().generateTheString(4)
    print(solution)

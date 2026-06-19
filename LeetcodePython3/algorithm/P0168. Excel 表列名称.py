#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 08:49
FileName: P0168. Excel 表列名称.py
Description:
"""
from string import ascii_uppercase


class Solution:
    def convertToTitle(self, column: int) -> str:
        ss = []
        while column > 0:
            column -= 1
            column, mod = divmod(column, 26)
            ss.append(ascii_uppercase[mod])
        return ''.join(ss)[::-1]


if __name__ == '__main__':
    solution = Solution().convertToTitle(column=2147483647)
    print(solution)

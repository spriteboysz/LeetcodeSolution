#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-18 23:23
FileName: P0171. Excel 表列序号
Description:
"""
from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for ch in columnTitle:
            num = num * 26 + ascii_uppercase.index(ch) + 1
        return num


if __name__ == '__main__':
    solution = Solution().titleToNumber('A')
    print(solution)

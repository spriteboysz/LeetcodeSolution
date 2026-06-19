#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 09:17
FileName: P0171. Excel 表列序号.py
Description:
"""


class Solution:
    def titleToNumber(self, column_title: str) -> int:
        num = 0
        for ch in column_title:
            num = num * 26 + ord(ch) - ord('A') + 1
        return num


if __name__ == '__main__':
    solution = Solution().titleToNumber('ZY')
    print(solution)

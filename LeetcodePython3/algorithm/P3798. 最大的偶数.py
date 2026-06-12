#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:48
FileName: P3798. 最大的偶数.py
Description:
"""


class Solution:
    def largestEven(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '2':
                return s[:i + 1]
        return ''


if __name__ == '__main__':
    solution = Solution().largestEven('221')
    print(solution)

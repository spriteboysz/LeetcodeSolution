#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-01-17 09:59
FileName: P3798. 最大的偶数.py
Description:
"""


class Solution:
    def largestEven(self, s: str) -> str:
        for i, ch in enumerate(s[::-1]):
            if int(ch) % 2 == 0:
                return s[:len(s) - i]
        return ''


if __name__ == '__main__':
    solution = Solution().largestEven('111')
    print(solution)

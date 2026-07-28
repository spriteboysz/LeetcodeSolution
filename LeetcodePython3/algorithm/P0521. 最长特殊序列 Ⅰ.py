#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:28
FileName: P0521. 最长特殊序列 Ⅰ.py
Description:
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))


if __name__ == '__main__':
    solution = Solution().findLUSlength('a', 'b')
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:14
FileName: P2278. 字母在字符串中的百分比.py
Description:
"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)


if __name__ == '__main__':
    solution = Solution().percentageLetter(s="foobar", letter="o")
    print(solution)

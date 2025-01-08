#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 22:24
FileName: P2278. 字母在字符串中的百分比
Description:
"""

from icecream import ic


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)


if __name__ == '__main__':
    solution = Solution().percentageLetter(s="foobar", letter="o")
    ic(solution)

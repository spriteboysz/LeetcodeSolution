#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 19:50
FileName: P1796. 字符串中第二大的数字.py
Description:
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(ch) for ch in s if ch.isdigit()}
        if len(digits) < 2:
            return -1
        return sorted(digits)[-2]


if __name__ == '__main__':
    solution = Solution().secondHighest(s="dfa12321afd")
    print(solution)

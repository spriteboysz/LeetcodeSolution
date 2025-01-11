#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 23:12
FileName: P1844. 将所有数字用字符替换
Description:
"""

from icecream import ic


class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(i, ch):
            if ch.isdigit():
                return chr(ord(s[i - 1]) + int(ch))
            return ch

        return ''.join([shift(i, ch) for i, ch in enumerate(s)])


if __name__ == '__main__':
    solution = Solution().replaceDigits("a1b2c3d4e")
    ic(solution)

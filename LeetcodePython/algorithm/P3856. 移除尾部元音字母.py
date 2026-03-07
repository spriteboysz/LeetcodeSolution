#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-07 14:39
FileName: P3856. 移除尾部元音字母.py
Description:
"""


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        ss = list(s)
        while ss and ss[-1] in 'aeiou':
            ss.pop()
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().trimTrailingVowels('baeiou')
    print(solution)

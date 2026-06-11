#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:52
FileName: P3120. 统计特殊字母的数量 I.py
Description:
"""

from string import ascii_lowercase, ascii_uppercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return sum(ch1 in word and ch2 in word for ch1, ch2 in zip(ascii_lowercase, ascii_uppercase))


if __name__ == '__main__':
    solution = Solution().numberOfSpecialChars(word="aaAbcBC")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 09:06
FileName: P3856. 移除尾部元音字母.py
Description:
"""


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in 'aeiou':
                return s[:i + 1]
        return ''


if __name__ == '__main__':
    solution = Solution().trimTrailingVowels(s="idea")
    print(solution)

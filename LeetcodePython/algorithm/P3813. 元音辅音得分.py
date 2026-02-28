#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-01-25 16:57
FileName: P3813. 元音辅音得分.py
Description:
"""


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 'aeiou'
        v = sum(ch in vowels for ch in s)
        c = sum(ch not in vowels and ch.isalpha() for ch in s)
        return v // c if c != 0 else 0


if __name__ == '__main__':
    solution = Solution().vowelConsonantScore("cooear")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 22:34
FileName: P2309. 兼具大小写的最好英文字母.py
Description:
"""
from string import ascii_uppercase, ascii_lowercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        for ch1, ch2 in zip(ascii_uppercase[::-1], ascii_lowercase[::-1]):
            if ch1 in s and ch2 in s:
                return ch1
        return ''


if __name__ == '__main__':
    solution = Solution().greatestLetter(s="arRAzFif")
    print(solution)

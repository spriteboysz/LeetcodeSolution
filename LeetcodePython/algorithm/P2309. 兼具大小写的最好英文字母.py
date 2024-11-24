#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 14:13
FileName: P2309. 兼具大小写的最好英文字母
Description:
"""
from string import ascii_lowercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(str(s))
        for ch in ascii_lowercase[::-1]:
            if ch in seen and ch.upper() in seen:
                return ch.upper()
        return ''


if __name__ == '__main__':
    solution = Solution().greatestLetter(s="arRAzFif")
    print(solution)

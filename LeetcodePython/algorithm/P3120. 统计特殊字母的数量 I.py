#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 20:49
FileName: P3120. 统计特殊字母的数量 I
Description:
"""
from string import ascii_lowercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set(list(word))
        return sum([ch in seen and ch.upper() in seen for ch in ascii_lowercase])


if __name__ == '__main__':
    solution = Solution().numberOfSpecialChars(word="aaAbcBC")
    print(solution)

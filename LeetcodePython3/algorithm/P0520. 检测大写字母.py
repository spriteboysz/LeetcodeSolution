#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 21:59
FileName: P0520. 检测大写字母.py
Description:
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.capitalize() == word or word.upper() == word or word.lower() == word


if __name__ == '__main__':
    solution = Solution().detectCapitalUse('g')
    print(solution)

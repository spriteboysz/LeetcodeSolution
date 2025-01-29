#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 22:38
FileName: P3136. 有效单词
Description:
"""

from icecream import ic


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = 'aeiouAEIOU'
        flag1, flag2 = False, False
        for ch in word:
            if not ch.isalnum():
                return False
            if ch in vowels:
                flag1 = True
            elif ch.isalpha():
                flag2 = True
        return flag1 and flag2


if __name__ == '__main__':
    solution = Solution().isValid(word="234Adas")
    ic(solution)

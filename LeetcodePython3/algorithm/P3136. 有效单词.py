#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 16:23
FileName: P3136. 有效单词.py
Description:
"""


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        flag1, flag2 = False, False
        for ch in word:
            if ch.isalpha():
                if ch.lower() in 'aeiou':
                    flag1 = True
                else:
                    flag2 = True
            elif not ch.isdigit():
                return False
        return flag1 and flag2


if __name__ == '__main__':
    solution = Solution().isValid(word="234Adas")
    print(solution)

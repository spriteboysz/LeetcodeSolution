#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:18
FileName: P2785. 将字符串中的元音字母排序.py
Description:
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        ss = list(s)
        vowels = sorted([ch for ch in ss if ch.lower() in 'aeiou'], reverse=True)
        for i, ch in enumerate(ss):
            if ch.lower() in 'aeiou':
                ss[i] = vowels.pop()
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().sortVowels(s = "lEetcOde")
    print(solution)

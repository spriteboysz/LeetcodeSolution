#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:38
FileName: P0345. 反转字符串中的元音字母.py
Description:
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch.lower() in 'aeiou']
        ss = list(s)
        for i, ch in enumerate(ss):
            if ch.lower() in 'aeiou':
                ss[i] = vowels.pop()
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().reverseVowels(s="leetcode")
    print(solution)

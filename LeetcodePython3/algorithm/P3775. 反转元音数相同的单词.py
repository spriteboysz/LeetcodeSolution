#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 09:58
FileName: algorithm/P3775. 反转元音数相同的单词.py
Description: 
"""
from functools import lru_cache


class Solution:
    def reverseWords(self, s: str) -> str:
        @lru_cache
        def calc(w):
            return sum(c in 'aeiou' for c in w)

        words = s.split()
        k = calc(words[0])
        return ' '.join(word[::-1] if i > 0 and calc(word) == k else word for i, word in enumerate(words))


if __name__ == '__main__':
    solution = Solution().reverseWords("book is nice")
    print('<None>' if solution is None else f'{solution=}')

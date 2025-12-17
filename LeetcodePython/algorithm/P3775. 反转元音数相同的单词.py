#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-17 22:08
FileName: P3775. 反转元音数相同的单词.py
Description:
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def calc(w):
            return sum(ch in vowels for ch in w)

        words = s.split()
        m = calc(words[0])
        return ' '.join(word[::-1] if i != 0 and m == calc(word) else word for i, word in enumerate(words))


if __name__ == '__main__':
    solution = Solution().reverseWords(s="cat and mice")
    print(solution)

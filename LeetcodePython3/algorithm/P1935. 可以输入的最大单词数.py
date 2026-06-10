#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:36
FileName: P1935. 可以输入的最大单词数.py
Description:
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(all(letter not in word for letter in brokenLetters) for word in text.strip().split())


if __name__ == '__main__':
    solution = Solution().canBeTypedWords(text="hello world", brokenLetters="ad")
    print(solution)

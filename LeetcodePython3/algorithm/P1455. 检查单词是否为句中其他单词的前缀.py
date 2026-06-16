#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 22:54
FileName: P1455. 检查单词是否为句中其他单词的前缀.py
Description:
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.strip().split()
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution().isPrefixOfWord(sentence="i love eating burger", searchWord="burg")
    print(solution)

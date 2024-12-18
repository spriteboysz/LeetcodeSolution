#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-17 23:20
FileName: P1455. 检查单词是否为句中其他单词的前缀
Description:
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.strip().split()):
            if word.startswith(searchWord):
                return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution().isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro")
    print(solution)

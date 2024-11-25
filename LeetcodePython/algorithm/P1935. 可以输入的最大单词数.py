#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 23:01
FileName: P1935. 可以输入的最大单词数
Description:
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        seen = set(brokenLetters)
        words = text.split()
        return sum([len(set(word) & seen) == 0 for word in words])


if __name__ == '__main__':
    solution = Solution().canBeTypedWords(text="hello world", brokenLetters="ad")
    print(solution)

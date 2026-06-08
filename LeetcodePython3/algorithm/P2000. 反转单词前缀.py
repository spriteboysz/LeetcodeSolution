#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:53
FileName: P2000. 反转单词前缀.py
Description:
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, w in enumerate(word):
            if w == ch:
                return word[:i + 1][::-1] + word[i + 1:]
        return word


if __name__ == '__main__':
    solution = Solution().reversePrefix(word="abcdefd", ch='d')
    print(solution)

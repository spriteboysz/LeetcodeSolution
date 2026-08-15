#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 11:02
FileName: algorithm/P1451. 重新排列句子中的单词.py
Description: 
"""


class Solution:
    def arrangeWords(self, text: str) -> str:
        words = sorted(text.lower().split(), key=len)
        return ' '.join(words).capitalize()


if __name__ == '__main__':
    solution = Solution().arrangeWords(text="Keep calm and code on")
    print(solution)

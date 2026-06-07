#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 11:44
FileName: P1078. Bigram 分词.py
Description:
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.strip().split()
        return [word for i, word in enumerate(words[2:], start=2) if first == words[i - 2] and second == words[i - 1]]


if __name__ == '__main__':
    solution = Solution().findOcurrences(text="we will we will rock you", first="we", second="will")
    print(solution)

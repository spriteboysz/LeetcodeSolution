#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 22:54
FileName: P2068. 检查两个字符串是否几乎相等.py
Description:
"""
from collections import Counter
from string import ascii_lowercase


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)
        return all(abs(counter1.get(ch, 0) - counter2.get(ch, 0)) <= 3 for ch in ascii_lowercase)


if __name__ == '__main__':
    solution = Solution().checkAlmostEquivalent(word1="abcdeef", word2="abaaacc")
    print(solution)

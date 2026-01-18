#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-01-17 10:21
FileName: P3805. 统计凯撒加密对数目.py
Description:
"""

from typing import List
from collections import Counter


class Solution:
    def countPairs(self, words: List[str]) -> int:
        def process(word):
            return ''.join(chr((ord(ch) + 26 - ord(word[0])) % 26 + ord('a')) for ch in word)

        counter = Counter(process(word) for word in words)
        return sum(v * (v - 1) // 2 for v in counter.values())


if __name__ == '__main__':
    s = Solution().countPairs(words=["ab", "aa", "za", "aa"])
    print(s)

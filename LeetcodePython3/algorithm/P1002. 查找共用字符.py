#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 11:26
FileName: P1002. 查找共用字符.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alphabet = [0] * 26
        for ch in words[0]:
            alphabet[ord(ch) - ord('a')] += 1
        for word in words[1:]:
            counter = Counter(word)
            for i in range(26):
                alphabet[i] = min(alphabet[i], counter.get(chr(ord('a') + i), 0))
        return sum([[chr(ord('a') + i)] * cnt for i, cnt in enumerate(alphabet)], [])


if __name__ == '__main__':
    solution = Solution().commonChars(words=["bella", "label", "roller"])
    print(solution)

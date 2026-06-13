#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 11:44
FileName: P0290. 单词规律.py
Description:
"""
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic1, dic2 = defaultdict(set), defaultdict(set)
        words = s.strip().split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            dic1[ch].add(word)
            dic2[word].add(ch)
        return all(len(el) == 1 for el in dic1.values()) and all(len(el) == 1 for el in dic2.values())


if __name__ == '__main__':
    solution = Solution().wordPattern(pattern="abba", s="dog cat cat dog")
    print(solution)

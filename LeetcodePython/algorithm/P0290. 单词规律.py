#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:12
FileName: P0290. 单词规律
Description:
"""
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        dic1, dic2 = defaultdict(set), defaultdict(set)
        for ch, word in zip(pattern, words):
            dic1[ch].add(word)
            dic2[word].add(ch)
        return all(map(lambda el: len(el) <= 1, [*dic1.values(), *dic2.values()]))


if __name__ == '__main__':
    solution = Solution().wordPattern(pattern="abba", s="dog cat cat dog")
    print(solution)

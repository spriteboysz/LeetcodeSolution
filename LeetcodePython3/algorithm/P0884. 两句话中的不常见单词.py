#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:53
FileName: P0884. 两句话中的不常见单词.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter1, counter2 = Counter(s1.split()), Counter(s2.split())
        uncommon = []
        for word in {*counter1.keys(), *counter2.keys()}:
            if counter1.get(word, 0) + counter2.get(word, 0) == 1:
                uncommon.append(word)
        return uncommon


if __name__ == '__main__':
    solution = Solution().uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 15:58
FileName: 面试题/面试题 17.11. 单词距离.py
Description: 
"""
from math import inf

from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        index1, index2 = inf, -inf
        distances = []
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            distances.append(abs(index1 - index2))
        return min(distances)


if __name__ == '__main__':
    solution = Solution().findClosest(
        words=["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"],
        word1="a", word2="student"
    )
    print('<None>' if solution is None else f'{solution=}')

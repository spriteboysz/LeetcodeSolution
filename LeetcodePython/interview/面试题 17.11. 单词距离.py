#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 21:08
FileName: interview/面试题 17.11. 单词距离.py
Description: 
"""
from typing import List
import math

from icecream import ic


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        minimum, index1, index2 = len(words) + 1, math.inf, -math.inf
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            if word == word2:
                index2 = i
            minimum = min(minimum, abs(index1 - index2))
        return minimum


if __name__ == '__main__':
    solution = Solution().findClosest(
        words=["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"],
        word1="a", word2="student")
    ic(solution)

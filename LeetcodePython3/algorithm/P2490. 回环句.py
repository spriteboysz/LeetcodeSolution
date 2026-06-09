#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 23:05
FileName: P2490. 回环句.py
Description:
"""
from itertools import pairwise


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for word1, word2 in pairwise(words):
            if word1[-1] != word2[0]:
                return False
        return words[0][0] == words[-1][-1]


if __name__ == '__main__':
    solution = Solution().isCircularSentence(sentence="leetcode exercises sound delightful")
    print(solution)

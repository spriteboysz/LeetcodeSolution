#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-12 11:20
FileName: algorithm/P1813. 句子相似性 III.py
Description: 
"""

from icecream import ic


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        if words1 == words2:
            return True
        if len(words1) == len(words2):
            return False
        words1, words2 = sorted([words1, words2], key=len)
        while words1 and (words1[0] == words2[0] or words1[-1] == words2[-1]):
            if words1[0] == words2[0]:
                words1.pop(0)
                words2.pop(0)
            if words1 and words1[-1] == words2[-1]:
                words1.pop()
                words2.pop()
        return not words1


if __name__ == '__main__':
    solution = Solution().areSentencesSimilar(sentence1="My name is Haley", sentence2="My Haley")
    ic(solution)

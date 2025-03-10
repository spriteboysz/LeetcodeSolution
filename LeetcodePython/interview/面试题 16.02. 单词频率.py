#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-10 22:52
FileName: interview/面试题 16.02. 单词频率.py
Description: 
"""
from collections import defaultdict
from typing import List

from icecream import ic


class WordsFrequency:

    def __init__(self, book: List[str]):
        self.dic = defaultdict(int)
        for word in book:
            self.dic[word] += 1

    def get(self, word: str) -> int:
        return self.dic.get(word, 0)


if __name__ == '__main__':
    solution = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    ic(solution.get('you'))
    ic(solution.get('i'))
    ic(solution.get('have'))

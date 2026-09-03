#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:33
FileName: 面试题/面试题 16.02. 单词频率.py
Description: 
"""
from collections import Counter
from typing import List


class WordsFrequency:

    def __init__(self, book: List[str]):
        self.counter = Counter(book)

    def get(self, word: str) -> int:
        return self.counter.get(word, 0)


if __name__ == '__main__':
    solution = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    print(solution.get('have'))

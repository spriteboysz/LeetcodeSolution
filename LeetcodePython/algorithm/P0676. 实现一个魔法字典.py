#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-12 12:18
FileName: algorithm/P0676. 实现一个魔法字典.py
Description: 
"""
from typing import List
from collections import defaultdict

from icecream import ic


class MagicDictionary:

    def __init__(self):
        self.dic = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dic[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.dic[len(searchWord)]:
            if word == searchWord:
                continue
            cnt = 0
            for ch1, ch2 in zip(word, searchWord):
                if ch1 != ch2:
                    cnt += 1
                if cnt > 1:
                    break
            else:
                return True
        return False


if __name__ == '__main__':
    magic_dictionary = MagicDictionary()
    magic_dictionary.buildDict(["hello", "leetcode"])
    ic(magic_dictionary.search('hello'))
    ic(magic_dictionary.search('hhllo'))
    ic(magic_dictionary.search('hell'))
    ic(magic_dictionary.search('leetcoded'))

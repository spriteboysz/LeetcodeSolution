#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 11:30
FileName: algorithm/P0211. 添加与搜索单词 - 数据结构设计.py
Description: 
"""
import re
from collections import defaultdict

from icecream import ic


class WordDictionary:

    def __init__(self):
        self.dic = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.dic[len(word)].append(word)

    def search(self, word: str) -> bool:
        text = '\n'.join(self.dic[len(word)])
        return bool(re.findall(word, text))


if __name__ == '__main__':
    word_dictionary = WordDictionary()
    word_dictionary.addWord('bad')
    word_dictionary.addWord('dad')
    word_dictionary.addWord('mad')
    ic(word_dictionary.search('pad'))
    ic(word_dictionary.search('.ad'))
    ic(word_dictionary.search('b..'))

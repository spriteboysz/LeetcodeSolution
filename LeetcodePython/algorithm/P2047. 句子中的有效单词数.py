#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-09 23:16
FileName: P2047. 句子中的有效单词数
Description:
"""

import re

from icecream import ic


class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile(r'^[a-z]*([a-z]-[a-z])?[a-z]*[!,.]?$')
        return sum([1 for word in sentence.strip().split() if pattern.match(word)])


if __name__ == '__main__':
    solution = Solution().countValidWords(sentence="alice and  bob are playing stone-game10")
    ic(solution)

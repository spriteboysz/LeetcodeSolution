#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-12 10:41
FileName: algorithm/P0792. 匹配子序列的单词数.py
Description: 
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        for word, cnt in Counter(words).items():
            i = 0
            for c in word:
                i = s.find(c, i) + 1
                if not i:
                    break
            else:
                res += cnt
        return res


if __name__ == '__main__':
    solution = Solution().numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"])
    ic(solution)

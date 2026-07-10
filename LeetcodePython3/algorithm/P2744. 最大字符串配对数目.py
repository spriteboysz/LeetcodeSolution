#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 23:13
FileName: P2744. 最大字符串配对数目.py
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)
        for word in words:
            dic[tuple(sorted(word))] += 1
        return list(dic.values()).count(2)


if __name__ == '__main__':
    solution = Solution().maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"])
    print(solution)

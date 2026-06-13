#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 11:38
FileName: P0205. 同构字符串.py
Description:
"""

from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = defaultdict(set), defaultdict(set)
        for ch1, ch2 in zip(s, t):
            dic1[ch1].add(ch2)
            dic2[ch2].add(ch1)
        return all(len(el) == 1 for el in dic1.values()) and all(len(el) == 1 for el in dic2.values())


if __name__ == '__main__':
    solution = Solution().isIsomorphic(s="egg", t="add")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:37
FileName: P2839. 判断通过操作能否让字符串相等 I.py
Description:
"""
from collections import defaultdict


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        dic0, dic1 = defaultdict(int), defaultdict(int)
        for i, (ch1, ch2) in enumerate(zip(s1, s2)):
            if i % 2 == 0:
                dic0[ch1] += 1
                dic0[ch2] -= 1
            else:
                dic1[ch1] += 1
                dic1[ch2] -= 1
        return all(v == 0 for v in dic0.values()) and all(v == 0 for v in dic1.values())


if __name__ == '__main__':
    solution = Solution().canBeEqual(s1="abcd", s2="cdab")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:58
FileName: P0389. 找不同.py
Description:
"""
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1, counter2 = Counter(s), Counter(t)
        for ch, cnt in counter2.items():
            if cnt - counter1.get(ch, 0) == 1:
                return ch
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().findTheDifference(s="abcd", t="abcde")
    print(solution)

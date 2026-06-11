#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 22:58
FileName: P3438. 找到字符串中合法的相邻数字.py
Description:
"""
from itertools import pairwise
from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)
        seen = {k for k, v in counter.items() if int(k) == v}
        for ch1, ch2 in pairwise(s):
            if ch1 != ch2 and ch1 in seen and ch2 in seen:
                return f'{ch1}{ch2}'
        return ''


if __name__ == '__main__':
    solution = Solution().findValidPair(s="2523533")
    print(solution)

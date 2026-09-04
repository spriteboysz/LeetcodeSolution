#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 14:10
FileName: 面试题/面试题 16.15. 珠玑妙算.py
Description: 
"""
from collections import defaultdict

from typing import List


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        dic1, dic2 = defaultdict(int), defaultdict(int)
        a, b = 0, 0
        for c1, c2 in zip(solution, guess):
            if c1 == c2:
                a += 1
            else:
                dic1[c1] += 1
                dic2[c2] += 1
        for c, cnt in dic1.items():
            b += min(cnt, dic2.get(c, 0))
        return [a, b]


if __name__ == '__main__':
    s = Solution().masterMind(solution="RGBY", guess="GGRR")
    print(s)

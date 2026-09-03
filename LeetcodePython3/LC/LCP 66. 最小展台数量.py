#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:24
FileName: LC/LCP 66. 最小展台数量.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        counter = Counter(demand[0])
        for s in demand[1:]:
            counter1 = Counter(s)
            for k, v in counter1.items():
                counter[k] = max(v, counter.get(k, 0))
        return sum(counter.values())


if __name__ == '__main__':
    solution = Solution().minNumBooths(["acd", "bed", "accd"])
    print(solution)

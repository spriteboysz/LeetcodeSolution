#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 08:41
FileName: P2103. 环和杆.py
Description:
"""
from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        dic = defaultdict(set)
        for i in range(0, len(rings), 2):
            color, key = rings[i:i + 2]
            dic[key].add(color)
        return sum(len(s) == 3 for s in dic.values())


if __name__ == '__main__':
    solution = Solution().countPoints(rings="B0B6G0R6R0R6G9")
    print(solution)

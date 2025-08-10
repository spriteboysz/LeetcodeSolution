#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-08-10 11:33
FileName: algorithm/P1247. 交换字符使得字符串相同.py
Description: 
"""
from collections import Counter
from icecream import ic


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        counter = Counter(x for x, y in zip(s1, s2) if x != y)
        diff = counter.get('x', 0) + counter.get('y', 0)
        if diff % 2 != 0:
            return -1
        return diff // 2 + counter.get('x', 0) % 2


if __name__ == '__main__':
    solution = Solution().minimumSwap(s1="xx", s2="yy")
    ic(solution)

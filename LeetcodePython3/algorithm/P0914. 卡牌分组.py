#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:36
FileName: P0914. 卡牌分组.py
Description:
"""
from collections import Counter
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = list(Counter(deck).values())
        if len(counter) == 1:
            return len(deck) >= 2
        minimum = gcd(*counter)
        if minimum == 1:
            return False
        return all(cnt % minimum == 0 for cnt in counter) and len(deck) % minimum == 0 and len(deck) // minimum >= 2


if __name__ == '__main__':
    solution = Solution().hasGroupsSizeX(deck=[1, 1, 1, 1, 2, 2, 2, 2, 2, 2])
    print(solution)

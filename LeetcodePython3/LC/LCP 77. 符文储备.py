#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 15:04
FileName: LC/LCP 77. 符文储备.py
Description: 
"""
from collections import Counter
from itertools import pairwise

from typing import List


class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        counter = Counter(runes)
        keys = sorted(counter.keys())
        maximum, curr = 0, counter.get(keys[0], 0)
        for a, b in pairwise(keys):
            if b - a == 1:
                curr += counter.get(b, 0)
            else:
                maximum = max(maximum, curr)
                curr = counter.get(b, 0)
        return max(maximum, curr)


if __name__ == '__main__':
    solution = Solution().runeReserve(runes=[1, 1, 3, 3, 2, 4])
    print('<None>' if solution is None else f'{solution=}')

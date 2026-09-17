#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 14:49
FileName: LC/LCP 72. 补给马车.py
Description: 
"""
from itertools import pairwise
from typing import List


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        n = len(supplies)
        while len(supplies) > n // 2:
            minimum = min(a + b for a, b in pairwise(supplies))
            for i in range(1, len(supplies)):
                if supplies[i - 1] + supplies[i] == minimum:
                    supplies[i - 1] = minimum
                    supplies[i] = None
                    break
            supplies = [supply for supply in supplies if supply is not None]
        return supplies


if __name__ == '__main__':
    solution = Solution().supplyWagon(supplies=[7, 3, 6, 1, 8])
    print('<None>' if solution is None else f'{solution=}')

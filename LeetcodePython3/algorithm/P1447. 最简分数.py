#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 15:41
FileName: algorithm/P1447. 最简分数.py
Description: 
"""
import math
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = []
        for b in range(2, n + 1):
            for a in range(1, b):
                if math.gcd(a, b) == 1:
                    fractions.append(f'{a}/{b}')
        return fractions


if __name__ == '__main__':
    solution = Solution().simplifiedFractions(4)
    print('<None>' if solution is None else f'{solution=}')

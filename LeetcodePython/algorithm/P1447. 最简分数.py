#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-03 22:51
FileName: algorithm/P1447. 最简分数.py
Description: 
"""
import math
from typing import List

from icecream import ic


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = set()
        for i in range(2, n + 1):
            for j in range(1, i):
                gcd = math.gcd(i, j)
                fractions.add(f'{j // gcd}/{i // gcd}')
        return list(fractions)


if __name__ == '__main__':
    solution = Solution().simplifiedFractions(4)
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 10:22
FileName: algorithm/LCP 02. 分式化简.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n, m = 0, 1
        for a in cont[::-1]:
            n, m = m, m * a + n
        return [m, n]


if __name__ == '__main__':
    solution = Solution().fraction([3, 2, 0, 2])
    ic(solution)

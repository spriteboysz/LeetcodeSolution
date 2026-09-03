#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 15:57
FileName: LC/LCR 188. 买卖芯片的最佳时机.py
Description: 
"""
from math import inf

from typing import List


class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        minimum, maximum = inf, 0
        for price in prices:
            minimum = min(minimum, price)
            maximum = max(maximum, price - minimum)
        return maximum


if __name__ == '__main__':
    solution = Solution().bestTiming(prices=[8, 12, 15, 7, 3, 10])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 9:22
FileName: LCR/LCR 188. 买卖芯片的最佳时机.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maximum, minimum = 0, prices[0]
        for price in prices:
            maximum = max(maximum, price - minimum)
            minimum = min(minimum, price)
        return maximum


if __name__ == '__main__':
    solution = Solution().bestTiming(prices=[8, 12, 15, 7, 3, 10])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 14:39
FileName: LC/LCR 161. 连续天数的最高销售额.py
Description: 
"""
from typing import List


class Solution:
    def maxSales(self, sales: List[int]) -> int:
        curr = maximum = sales[0]
        for i, sale in enumerate(sales[1:], start=1):
            curr = max(curr + sale, sale)
            maximum = max(maximum, curr)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxSales([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print('<None>' if not solution else f'{solution=}')

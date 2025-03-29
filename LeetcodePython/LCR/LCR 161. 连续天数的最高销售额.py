#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-28 21:25
FileName: LCR/LCR 161. 连续天数的最高销售额.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maxSales(self, sales: List[int]) -> int:
        acc, m, maximum = 0, 0, -10010
        for sale in sales:
            acc += sale
            maximum = max(maximum, acc - m)
            m = min(m, acc)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxSales(sales=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 22:21
FileName: P0121. 买卖股票的最佳时机
Description:
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr, maximum = prices[0], 0
        for price in prices:
            maximum = max(maximum, price - curr)
            curr = min(curr, price)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print(solution)

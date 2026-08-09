#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 18:14
FileName: P4014. 应用折扣后的最低总价.py
Description:
"""


class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        for i, (price, discount) in enumerate(zip(prices, discounts)):
            prices[i] = price * (100 - discount) / 100
        return sum(prices)


if __name__ == '__main__':
    solution = Solution().minPrice(prices=[10, 30, 21], discounts=[50, 60])
    print(solution)

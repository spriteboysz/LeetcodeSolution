#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 21:18
FileName: P1475. 商品折扣后的最终价格
Description:
"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, price1 in enumerate(prices):
            for price2 in prices[i + 1:]:
                if price2 <= price1:
                    prices[i] -= price2
                    break
        return prices


if __name__ == '__main__':
    solution = Solution().finalPrices(prices=[8, 4, 6, 2, 3])
    print(solution)

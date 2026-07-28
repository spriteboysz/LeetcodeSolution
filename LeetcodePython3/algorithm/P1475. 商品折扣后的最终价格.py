#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:32
FileName: P1475. 商品折扣后的最终价格.py
Description:
"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, price1 in enumerate(prices):
            for price2 in prices[i + 1:]:
                if price1 >= price2:
                    ans.append(price1 - price2)
                    break
            else:
                ans.append(price1)
        return ans


if __name__ == '__main__':
    solution = Solution().finalPrices(prices=[8, 4, 6, 2, 3])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 09:20
FileName: P2706. 购买两块巧克力
Description:
"""
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if (balance := money - sum(prices[:2])) >= 0:
            return balance
        return money


if __name__ == '__main__':
    solution = Solution().buyChoco(prices=[1, 2, 2], money=3)
    print(solution)

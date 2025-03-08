#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 22:26
FileName: LCR/P2806. 取整购买后的账户余额.py
Description: 
"""

from icecream import ic


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount + 5) // 10 * 10


if __name__ == '__main__':
    solution = Solution().accountBalanceAfterPurchase(15)
    ic(solution)

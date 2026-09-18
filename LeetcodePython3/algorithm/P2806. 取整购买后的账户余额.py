#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 15:22
FileName: algorithm/P2806. 取整购买后的账户余额.py
Description: 
"""


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount + 5) // 10 * 10


if __name__ == '__main__':
    solution = Solution().accountBalanceAfterPurchase(9)
    print('<None>' if solution is None else f'{solution=}')

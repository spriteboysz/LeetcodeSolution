#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-22 23:08
FileName: P2706. 购买两块巧克力.py
Description:
"""
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        acc = sum(sorted(prices)[:2])
        return money if acc > money else money - acc


if __name__ == '__main__':
    solution = Solution().buyChoco([1, 2, 2], 3)
    print(solution)

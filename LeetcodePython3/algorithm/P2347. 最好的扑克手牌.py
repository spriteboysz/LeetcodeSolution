#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:13
FileName: P2347. 最好的扑克手牌.py
Description:
"""
from typing import List, Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        maximum = max(Counter(ranks).values())
        if maximum >= 3:
            return "Three of a Kind"
        if maximum >= 2:
            return "Pair"
        if len(set(ranks)) == 5:
            return "High Card"
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().bestHand(ranks=[4, 4, 2, 4, 4], suits=["d", "a", "a", "b", "c"])
    print(solution)

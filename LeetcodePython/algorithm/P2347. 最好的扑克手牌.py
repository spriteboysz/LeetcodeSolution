#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 22:30
FileName: P2347. 最好的扑克手牌
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        counter = Counter(ranks)
        maximum = max(counter.values())
        if maximum >= 3:
            return 'Three of a Kind'
        if maximum == 2:
            return 'Pair'
        return 'High Card'


if __name__ == '__main__':
    solution = Solution().bestHand(ranks=[13, 2, 3, 1, 9], suits=["a", "a", "a", "a", "a"])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 13:49
FileName: algorithm/P2073. 买票需要的时间.py
Description: 
"""
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        for i, ticket in enumerate(tickets):
            if i <= k:
                cnt += min(ticket, tickets[k])
            else:
                cnt += min(ticket, tickets[k] - 1)
        return cnt


if __name__ == '__main__':
    solution = Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2)
    print('<None>' if solution is None else f'{solution=}')

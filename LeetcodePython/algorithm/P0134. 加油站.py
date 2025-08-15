#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-08-10 17:38
FileName: algorithm/P0134. 加油站.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n, start, total = len(gas), 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start, total = i + 1, 0
        return start


if __name__ == '__main__':
    solution = Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
    ic(solution)

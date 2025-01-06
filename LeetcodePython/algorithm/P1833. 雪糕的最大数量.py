#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-06 23:28
FileName: P1833. 雪糕的最大数量
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, cost in enumerate(costs):
            if coins >= cost:
                coins -= cost
            else:
                return i
        return len(costs)


if __name__ == '__main__':
    solution = Solution().maxIceCream(costs=[1, 3, 2, 4, 1], coins=7)
    ic(solution)

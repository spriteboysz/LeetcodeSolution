#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 20:54
FileName: LCP 06. 拿硬币
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((coin + 1) // 2 for coin in coins)


if __name__ == '__main__':
    solution = Solution().minCount([2, 3, 10])
    ic(solution)

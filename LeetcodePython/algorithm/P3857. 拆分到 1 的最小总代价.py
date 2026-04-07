#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-07 22:49
FileName: P3857. 拆分到 1 的最小总代价.py
Description:
"""
from functools import lru_cache
from math import ceil, floor


class Solution:
    @lru_cache
    def minCost(self, n: int) -> int:
        if n == 1:
            return 0
        a, b = ceil(n / 2), floor(n / 2)
        return self.minCost(a) + self.minCost(b) + a * b


if __name__ == '__main__':
    solution = Solution().minCost(4)
    print(solution)

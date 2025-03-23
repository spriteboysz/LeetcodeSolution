#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 18:14
FileName: algorithm/P3492. 船上可以装载的最大集装箱数量.py
Description: 
"""

from icecream import ic


class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(maxWeight // w, n * n)


if __name__ == '__main__':
    solution = Solution().maxContainers(n=3, w=5, maxWeight=20)
    ic(solution)

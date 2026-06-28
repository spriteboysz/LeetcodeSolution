#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 20:03
FileName: P3492. 船上可以装载的最大集装箱数量.py
Description:
"""


class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)


if __name__ == '__main__':
    solution = Solution().maxContainers(n=2, w=3, maxWeight=15)
    print(solution)

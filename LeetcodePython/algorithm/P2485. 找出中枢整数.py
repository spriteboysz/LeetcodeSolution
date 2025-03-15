#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-14 23:01
FileName: algorithm/P2485. 找出中枢整数.py
Description: 
"""

from icecream import ic


class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(1, n + 1):
            if sum(range(1, n + 1)) + x == sum(range(1, x + 1)) * 2:
                return x
        return -1


if __name__ == '__main__':
    solution = Solution().pivotInteger(8)
    ic(solution)

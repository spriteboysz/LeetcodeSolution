#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-05 11:28
FileName: algorithm/P3536. 两个数字的最大乘积.py
Description: 
"""

from icecream import ic


class Solution:
    def maxProduct(self, n: int) -> int:
        ss = str(n)
        maximum = 0
        for i, a in enumerate(ss):
            for b in ss[:i]:
                maximum = max(maximum, int(a) * int(b))
        return maximum


if __name__ == '__main__':
    solution = Solution().maxProduct(31)
    ic(solution)

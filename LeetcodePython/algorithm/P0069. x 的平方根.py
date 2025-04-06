#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-06 16:33
FileName: algorithm/P0069. x 的平方根.py
Description: 
"""

from icecream import ic


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)


if __name__ == '__main__':
    solution = Solution().mySqrt(8)
    ic(solution)

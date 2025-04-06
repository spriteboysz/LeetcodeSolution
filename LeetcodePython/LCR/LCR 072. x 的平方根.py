#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-06 16:34
FileName: LCR/LCR 072. x 的平方根.py
Description: 
"""

from icecream import ic


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid >= x:
                right = mid
            else:
                left = mid + 1
        return left if left * left == x else left - 1


if __name__ == '__main__':
    solution = Solution().mySqrt(8)
    ic(solution)

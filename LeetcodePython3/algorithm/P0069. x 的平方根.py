#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 17:32
FileName: P0069. x 的平方根.py
Description:
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        while s * s <= x:
            s += 1
            if s * s > x:
                return s - 1
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().mySqrt(8)
    print(solution)

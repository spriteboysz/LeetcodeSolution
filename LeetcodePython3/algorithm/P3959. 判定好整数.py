#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:42
FileName: P3959. 判定好整数.py
Description:
"""


class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = [int(digit) for digit in str(n)]
        return sum(d * d for d in digits) - sum(digits) >= 50


if __name__ == '__main__':
    solution = Solution().checkGoodInteger(1000)
    print(solution)

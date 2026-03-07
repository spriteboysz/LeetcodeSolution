#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-07 15:02
FileName: P3751. 范围内总波动值 I.py
Description:
"""


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(num):
            ss = str(num)
            return sum(
                left > digit < right or left < digit > right for left, digit, right in zip(ss[:-2], ss[1:-1], ss[2:]))

        return sum(calc(i) for i in range(max(100, num1), num2 + 1))


if __name__ == '__main__':
    s = Solution().totalWaviness(120, 130)
    print(s)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 16:21
FileName: P3099. 哈沙德数.py
Description:
"""


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(int(digit) for digit in str(x))
        return s if x % s == 0 else -1


if __name__ == '__main__':
    solution = Solution().sumOfTheDigitsOfHarshadNumber(18)
    print(solution)

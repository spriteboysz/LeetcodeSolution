#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 20:52
FileName: P2520. 统计能整除数字的位数.py
Description:
"""


class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(digit) == 0 for digit in str(num))


if __name__ == '__main__':
    solution = Solution().countDigits(1248)
    print(solution)

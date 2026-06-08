#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:12
FileName: P2264. 字符串中最大的 3 位相同数字.py
Description:
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            if str(digit) * 3 in num:
                return str(digit) * 3
        return ''


if __name__ == '__main__':
    solution = Solution().largestGoodInteger(num="2300019")
    print(solution)

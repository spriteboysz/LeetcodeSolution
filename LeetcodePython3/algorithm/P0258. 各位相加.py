#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:05
FileName: P0258. 各位相加.py
Description:
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(map(int, str(num)))
        return num


if __name__ == '__main__':
    solution = Solution().addDigits(38)
    print(solution)

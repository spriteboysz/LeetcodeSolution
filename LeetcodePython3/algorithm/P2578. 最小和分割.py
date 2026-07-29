#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 23:25
FileName: P2578. 最小和分割.py
Description:
"""


class Solution:
    def splitNum(self, num: int) -> int:
        def calc(nums):
            return sum(digit * 10 ** i for i, digit in enumerate(nums[::-1]))

        digits = sorted(int(digit) for digit in str(num))
        return calc(digits[::2]) + calc(digits[1::2])


if __name__ == '__main__':
    solution = Solution().splitNum(687)
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 17:48
FileName: P2160. 拆分数位后四位数字的最小和.py
Description:
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(int(digit) for digit in str(num))
        return sum(digits[:2]) * 10 + sum(digits[2:])


if __name__ == '__main__':
    solution = Solution().minimumSum(4009)
    print(solution)

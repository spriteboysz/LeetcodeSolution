#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-21 23:02
FileName: P0788. 旋转数字.py
Description:
"""


class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n + 1):
            digits = [int(digit) for digit in str(num)]
            if any(num in digits for num in [3, 4, 7]):
                continue
            if all(num not in digits for num in [2, 5, 6, 9]):
                continue
            count += 1
        return count


if __name__ == '__main__':
    solution = Solution().rotatedDigits(10)
    print(solution)

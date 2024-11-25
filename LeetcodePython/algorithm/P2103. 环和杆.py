#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-25 22:46
FileName: P2103. 环和杆
Description:
"""


class Solution:
    def countPoints(self, rings: str) -> int:
        digits = [0] * 10
        colors = {'R': 1, 'G': 2, 'B': 4}
        for i in range(0, len(rings), 2):
            color, digit = rings[i], int(rings[i + 1])
            digits[digit] |= colors.get(color)
        return sum([digit == 7 for digit in digits])


if __name__ == '__main__':
    solution = Solution().countPoints(rings="B0B6G0R6R0R6G9")
    print(solution)

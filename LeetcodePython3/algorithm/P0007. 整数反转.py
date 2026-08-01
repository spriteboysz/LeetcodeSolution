#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-30 22:35
FileName: P0007. 整数反转.py
Description:
"""


class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        if -2 ** 31 <= x <= 2 ** 31 - 1:
            return x
        return 0


if __name__ == '__main__':
    solution = Solution().reverse(-123)
    print(solution)

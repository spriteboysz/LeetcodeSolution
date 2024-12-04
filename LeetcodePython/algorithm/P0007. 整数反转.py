#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-03 22:56
FileName: P0007. 整数反转
Description:
"""


class Solution:
    def reverse(self, x: int) -> int:
        negative = (x < 0)
        val = int(str(abs(x))[::-1])
        val = val if not negative else -val
        if -2 ** 31 <= val <= 2 ** 31 + 1:
            return val
        return 0


if __name__ == '__main__':
    solution = Solution().reverse(-200)
    print(solution)

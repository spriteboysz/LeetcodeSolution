#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:26
FileName: P0342. 4的幂.py
Description:
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n and n % 4 == 0:
            n //= 4
        return n == 1


if __name__ == '__main__':
    solution = Solution().isPowerOfFour(64)
    print(solution)

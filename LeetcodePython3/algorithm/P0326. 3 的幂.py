#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:24
FileName: P0326. 3 的幂.py
Description:
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n and n % 3 == 0:
            n //= 3
        return n == 1


if __name__ == '__main__':
    solution = Solution().isPowerOfThree(27)
    print(solution)

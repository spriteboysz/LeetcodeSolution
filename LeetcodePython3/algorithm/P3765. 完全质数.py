#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-29 21:42
FileName: P3765. 完全质数.py
Description:
"""
from functools import lru_cache


class Solution:
    def completePrime(self, num: int) -> bool:
        @lru_cache
        def check(n):
            n = int(n)
            if n <= 1:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            return all(n % j != 0 for j in range(5, int(n ** 0.5) + 1))

        ss = str(num)
        return all(check(ss[:i + 1]) and check(ss[i:]) for i in range(len(ss)))


if __name__ == '__main__':
    solution = Solution().completePrime(232)
    print(solution)

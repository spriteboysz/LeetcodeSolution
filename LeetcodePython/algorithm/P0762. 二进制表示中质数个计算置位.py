#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-07 23:16
FileName: LCR/P0762. 二进制表示中质数个计算置位.py
Description: 
"""
from functools import lru_cache

from icecream import ic


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        @lru_cache
        def check(num):
            if num <= 1:
                return False
            return all(num % i != 0 for i in range(2, num))

        return sum(check(num.bit_count()) for num in range(left, right + 1))


if __name__ == '__main__':
    solution = Solution().countPrimeSetBits(6, 10)
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-24 22:15
FileName: P0762. 二进制表示中质数个计算置位.py
Description:
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(num.bit_count() in primes for num in range(left, right + 1))


if __name__ == '__main__':
    solution = Solution().countPrimeSetBits(6, 10)
    print(solution)

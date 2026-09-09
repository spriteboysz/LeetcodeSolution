#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 16:20
FileName: algorithm/P0172. 阶乘后的零.py
Description: 
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n:
            n //= 5
            cnt += n
        return cnt


if __name__ == '__main__':
    solution = Solution().trailingZeroes(5)
    print('<None>' if not solution else f'{solution=}')

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 08:46
FileName: 面试题/面试题 16.05. 阶乘尾数.py
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
    solution = Solution().trailingZeroes(100)
    print('<None>' if not solution else f'{solution=}')

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 11:29
FileName: 面试题/面试题 05.01. 插入.py
Description: 
"""


class Solution:
    def insertBits(self, n: int, m: int, i: int, j: int) -> int:
        def func(num, k):
            return list(bin(num)[2:].zfill(k)[::-1])

        ss = func(n, 32)
        ss[i:j + 1] = func(m, j - i + 1)
        return int(''.join(ss[::-1]), 2)


if __name__ == '__main__':
    solution = Solution().insertBits(1024, 19, 2, 6)
    print('<None>' if not solution else f'{solution=}')

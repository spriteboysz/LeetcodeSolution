#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 16:19
FileName: algorithm/P3226. 使两个整数相等的位更改次数.py
Description: 
"""


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        s1, s2 = bin(n)[2:].zfill(32), bin(k)[2:].zfill(32)
        cnt = 0
        for c1, c2 in zip(s1, s2):
            if c2 == '1' and c1 != '1':
                return -1
            if c1 != c2:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minChanges(n=89140, k=7200)
    print('<None>' if solution is None else f'{solution=}')

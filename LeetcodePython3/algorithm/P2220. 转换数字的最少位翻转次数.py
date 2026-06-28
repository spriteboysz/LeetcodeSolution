#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-27 22:05
FileName: P2220. 转换数字的最少位翻转次数.py
Description:
"""
from itertools import zip_longest


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        for ch1, ch2 in zip_longest(bin(start)[2:][::-1], bin(goal)[2:][::-1], fillvalue='0'):
            if ch1 != ch2:
                print(ch1, ch2)
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minBitFlips(10, 82)
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:06
FileName: P0461. 汉明距离.py
Description:
"""
from itertools import zip_longest


class Solution:
    @staticmethod
    def calc(num: int):
        return bin(num)[2:][::-1]

    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        for ch1, ch2 in zip_longest(self.calc(x), self.calc(y), fillvalue='0'):
            if ch1 != ch2:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().hammingDistance(1, 4)
    print(solution)

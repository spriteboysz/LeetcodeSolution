#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-24 22:08
FileName: P3918. 数与其逆序数之间的质数和.py
Description:
"""


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        left, right = sorted([n, int(str(n)[::-1])])
        flags = [True] * (right + 1)
        flags[0] = flags[1] = False
        for i in range(2, right + 1):
            if not flags[i]:
                continue
            for j in range(i * i, right + 1, i):
                flags[j] = False
        return sum(i for i, flag in enumerate(flags) if flag and i >= left)


if __name__ == '__main__':
    solution = Solution().sumOfPrimesInRange(13)
    print(solution)

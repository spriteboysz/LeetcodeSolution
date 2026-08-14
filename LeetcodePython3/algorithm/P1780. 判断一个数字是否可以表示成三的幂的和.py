#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-11 22:44
FileName: P1780. 判断一个数字是否可以表示成三的幂的和.py
Description:
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        digits = []
        while n >= 3:
            n, mod = divmod(n, 3)
            digits.append(mod)
        if n:
            digits.append(n)
        return 2 not in digits


if __name__ == '__main__':
    solution = Solution().checkPowersOfThree(91)
    print(solution)

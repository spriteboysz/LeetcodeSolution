#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 21:45
FileName: P3750. 最少反转次数得到翻转二进制字符串.py
Description:
"""


class Solution:
    def minimumFlips(self, n: int) -> int:
        s1 = bin(n)[2:]
        s2 = s1[::-1]
        return sum(el1 != el2 for el1, el2 in zip(s1, s2))


if __name__ == '__main__':
    s = Solution().minimumFlips(10)
    print(s)

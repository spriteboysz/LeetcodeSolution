#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 22:47
FileName: P3750. 最少翻转次数得到反转二进制字符串.py
Description:
"""


class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        return sum(ch1 != ch2 for ch1, ch2 in zip(s, s[::-1]))


if __name__ == '__main__':
    solution = Solution().minimumFlips(10)
    print(solution)

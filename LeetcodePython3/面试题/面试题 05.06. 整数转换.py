#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 11:33
FileName: 面试题/面试题 05.06. 整数转换.py
Description: 
"""


class Solution:
    def convertInteger(self, a: int, b: int) -> int:
        def convert(num):
            if num < 0:
                num = bin(-num - 1)[2:].zfill(32)
                num = ''.join('1' if d == '0' else '0' for d in str(num))
            else:
                num = bin(num)[2:].zfill(32)
            return num

        bin1, bin2 = convert(a), convert(b)
        return sum(b1 != b2 for b1, b2 in zip(bin1, bin2))


if __name__ == '__main__':
    solution = Solution().convertInteger(826966453, -729934991)
    print(solution)

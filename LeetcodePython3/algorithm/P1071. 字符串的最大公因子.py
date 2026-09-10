#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 16:16
FileName: algorithm/P1071. 字符串的最大公因子.py
Description: 
"""

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            m = math.gcd(len(str1), len(str2))
            return str1[:m]
        return ''


if __name__ == '__main__':
    solution = Solution().gcdOfStrings(str1="ABABAB", str2="ABAB")
    print('<None>' if solution is None else f'{solution=}')

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 11:30
FileName: P1071. 字符串的最大公因子
Description:
"""
import math

from icecream import ic


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ''


if __name__ == '__main__':
    solution = Solution().gcdOfStrings(str1="ABABAB", str2="ABAB")
    ic(solution)

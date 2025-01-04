#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 22:04
FileName: P2384. 最大回文数字
Description:
"""
from collections import defaultdict
from string import digits

from icecream import ic


class Solution:
    def largestPalindromic(self, num: str) -> str:
        dic = defaultdict(int)
        for digit in num:
            dic[digit] += 1
        ss, mid = '', ''
        for digit in digits[::-1]:
            if dic[digit] > 1:
                ss += digit * (dic[digit] // 2)
            if not mid and dic[digit] % 2 == 1:
                mid = digit
        return (ss + mid + ss[::-1]).strip('0') or '0'


if __name__ == '__main__':
    solution = Solution().largestPalindromic(num="00")
    ic(solution)

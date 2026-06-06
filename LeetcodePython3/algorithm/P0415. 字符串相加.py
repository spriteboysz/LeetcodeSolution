#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 20:17
FileName: P0415. 字符串相加.py
Description:
"""
from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans, carry = [], 0
        for digit1, digit2 in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            carry, mod = divmod(int(digit1) + int(digit2) + carry, 10)
            ans.append(mod)
        if carry:
            ans.append(carry)
        return ''.join(map(str, ans[::-1]))


if __name__ == '__main__':
    solution = Solution().addStrings(num1="456", num2="77")
    print(solution)

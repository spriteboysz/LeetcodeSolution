#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 17:12
FileName: P0067. 二进制求和.py
Description:
"""

from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0
        for digit1, digit2 in zip_longest(a[::-1], b[::-1], fillvalue=0):
            carry, mod = divmod(int(digit1) + int(digit2) + carry, 2)
            ans.append(mod)
        if carry:
            ans.append(carry)
        return ''.join(map(str, ans[::-1]))


if __name__ == '__main__':
    solution = Solution().addBinary('10', '1')
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 18:01
FileName: P0067. 二进制求和
Description:
"""
from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s, carry = [], 0
        for a1, b1 in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            carry += int(a1) + int(b1)
            carry, mod = divmod(carry, 2)
            s.append(mod)
        if carry:
            s.append(carry)
        return ''.join(map(str, s[::-1]))


if __name__ == '__main__':
    solution = Solution().addBinary('11', '11')
    print(solution)

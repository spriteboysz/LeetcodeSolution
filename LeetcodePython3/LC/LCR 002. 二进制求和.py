#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 13:47
FileName: LC/LCR 002. 二进制求和.py
Description: 
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s1, s2, carry = [int(digit) for digit in a], [int(digit) for digit in b], 0
        ans = []
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            carry, mod = divmod(carry, 2)
            ans.append(mod)
        return ''.join(map(str, ans[::-1]))


if __name__ == '__main__':
    solution = Solution().addBinary('1', '1')
    print(solution)

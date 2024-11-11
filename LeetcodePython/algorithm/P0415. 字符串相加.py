#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:21
FileName: P0415. 字符串相加
Description:
"""
from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums, carry = [], 0
        for ch1, ch2 in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            carry += int(ch1) + int(ch2)
            carry, mod = divmod(carry, 10)
            nums.append(str(mod))
        if carry:
            nums.append(str(carry))
        return ''.join(nums[::-1])


if __name__ == '__main__':
    solution = Solution().addStrings(num1="456", num2="77")
    print(solution)

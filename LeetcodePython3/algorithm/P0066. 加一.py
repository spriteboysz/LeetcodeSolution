#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 17:02
FileName: P0066. 加一.py
Description:
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        for digit in digits[::-1]:
            carry, mod = divmod(digit + carry, 10)
            result.append(mod)
        if carry:
            result.append(carry)
        return result[::-1]


if __name__ == '__main__':
    solution = Solution().plusOne([8, 9, 9])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 00:23
FileName: P0989. 数组形式的整数加法.py
Description:
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result, carry = [], k
        for digit in num[::-1]:
            carry, mod = divmod(digit + carry, 10)
            result.append(mod)
        if carry:
            result.extend([int(digit) for digit in str(carry)[::-1]])
        return result[::-1]


if __name__ == '__main__':
    solution = Solution().addToArrayForm(num=[0], k=806)
    print(solution)

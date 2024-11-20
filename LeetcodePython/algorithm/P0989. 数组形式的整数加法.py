#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-20 22:42
FileName: P0989. 数组形式的整数加法
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
            result.extend(map(int, list(str(carry)[::-1])))
        return result[::-1]


if __name__ == '__main__':
    solution = Solution().addToArrayForm(num=[5], k=101)
    print(solution)

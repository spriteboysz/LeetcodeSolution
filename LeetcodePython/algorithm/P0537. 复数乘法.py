#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 17:03
FileName: P0537. 复数乘法
Description:
"""

from icecream import ic


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        return f'{a * c - b * d}+{a * d + b * c}i'


if __name__ == '__main__':
    solution = Solution().complexNumberMultiply(num1="1+-1i", num2="1+-1i")
    ic(solution)

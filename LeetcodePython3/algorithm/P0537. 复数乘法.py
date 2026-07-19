#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:21
FileName: P0537. 复数乘法.py
Description:
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        return f'{real}+{imag}i'


if __name__ == '__main__':
    solution = Solution().complexNumberMultiply(num1="1+1i", num2="1+1i")
    print(solution)

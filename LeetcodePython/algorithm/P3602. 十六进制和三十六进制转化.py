#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-11 21:00
FileName: algorithm/P3602. 十六进制和三十六进制转化.py
Description: 
"""

from icecream import ic
from string import ascii_uppercase, digits


class Solution:
    def concatHex36(self, n: int) -> str:
        alphabet = digits + ascii_uppercase

        def process(num, base):
            ss = ''
            while num // base:
                num, mod = divmod(num, base)
                ss += alphabet[mod]
            ss += alphabet[num % base]
            return  ss[::-1]

        return process(n ** 2, 16) + process(n ** 3, 36)


if __name__ == '__main__':
    solution = Solution().concatHex36(1)
    ic(solution)

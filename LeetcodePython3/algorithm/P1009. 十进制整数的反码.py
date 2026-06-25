#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:19
FileName: P1009. 十进制整数的反码.py
Description:
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join(str(1 - int(ch)) for ch in bin(n)[2:]), 2)


if __name__ == '__main__':
    solution = Solution().bitwiseComplement(10)
    print(solution)

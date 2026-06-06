#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:18
FileName: P0190. 颠倒二进制位.py
Description:
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


if __name__ == '__main__':
    solution = Solution().reverseBits(43261596)
    print(solution)

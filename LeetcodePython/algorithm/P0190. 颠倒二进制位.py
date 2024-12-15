#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 17:34
FileName: P0190. 颠倒二进制位
Description:
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)


if __name__ == '__main__':
    solution = Solution().reverseBits(int('00000010100101000001111010011100', 2))
    print(solution)

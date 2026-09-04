#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 14:26
FileName: 面试题/面试题 05.03. 翻转数位.py
Description: 
"""
from itertools import pairwise


class Solution:
    def reverseBits(self, num: int) -> int:
        def convert(n):
            if n < 0:
                n = bin(-n - 1)[2:].zfill(32)
                n = ''.join('1' if d == '0' else '0' for d in str(n))
            else:
                n = bin(n)[2:].zfill(32)
            return n

        if num == -1:
            return 32

        s = convert(num)
        ss = s.split('0')
        return max(len(a) + len(b) for a, b in pairwise(ss)) + 1


if __name__ == '__main__':
    solution = Solution().reverseBits(-1)
    print(solution)

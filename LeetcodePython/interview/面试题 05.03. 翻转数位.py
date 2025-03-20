#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-18 23:04
FileName: interview/面试题 05.03. 翻转数位.py
Description: 
"""

from icecream import ic


class Solution:
    def reverseBits(self, num: int) -> int:
        if num < 0:
            num += (1 << 32)
        ss = bin(num)[2:].split('0')
        if len(ss) == 0:
            return 1
        if len(ss) == 1:
            return min(32, len(ss[0]) + 1)
        return max(len(ss[i - 1]) + len(ss[i]) for i in range(1, len(ss))) + 1


if __name__ == '__main__':
    solution = Solution().reverseBits(-1)
    ic(solution)

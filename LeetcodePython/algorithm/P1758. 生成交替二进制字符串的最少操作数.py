#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-07 23:30
FileName: LCR/P1758. 生成交替二进制字符串的最少操作数.py
Description: 
"""

from icecream import ic


class Solution:
    def minOperations(self, s: str) -> int:
        def process(ss):
            return sum(ch1 != ch2 for ch1, ch2 in zip(s, ss))

        s1, s2 = ('10' * len(s))[:len(s)], ('01' * len(s))[:len(s)]
        return min(process(s1), process(s2))


if __name__ == '__main__':
    solution = Solution().minOperations('0100')
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 16:32
FileName: algorithm/P1758. 生成交替二进制字符串的最少操作数.py
Description: 
"""


class Solution:
    def minOperations(self, s: str) -> int:
        def calc(str1, str2):
            return sum(c1 != c2 for c1, c2 in zip(str1, str2))

        s1 = ('01' * len(s))[:len(s)]
        s2 = ('10' * len(s))[:len(s)]
        return min(calc(s, s1), calc(s, s2))


if __name__ == '__main__':
    solution = Solution().minOperations('0100')
    print('<None>' if solution is None else f'{solution=}')

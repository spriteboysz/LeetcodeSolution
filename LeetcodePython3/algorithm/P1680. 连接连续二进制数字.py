#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 10:40
FileName: algorithm/P1680. 连接连续二进制数字.py
Description: 
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = 0
        for i in range(1, n + 1):
            m = len(bin(i)) - 2
            num = ((num << m) + i) % (10 ** 9 + 7)
        return num


if __name__ == '__main__':
    solution = Solution().concatenatedBinary(12)
    print('<None>' if solution is None else f'{solution=}')

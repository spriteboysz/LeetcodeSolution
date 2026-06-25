#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:11
FileName: P0693. 交替位二进制数.py
Description:
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return '00' not in bin(n) and '11' not in bin(n)


if __name__ == '__main__':
    solution = Solution().hasAlternatingBits(5)
    print(solution)

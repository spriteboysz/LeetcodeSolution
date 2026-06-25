#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-24 23:22
FileName: P476. 数字的补数.py
Description:
"""


class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(map(str, (1 - int(ch) for ch in bin(num)[2:]))), 2)


if __name__ == '__main__':
    solution = Solution().findComplement(5)
    print(solution)

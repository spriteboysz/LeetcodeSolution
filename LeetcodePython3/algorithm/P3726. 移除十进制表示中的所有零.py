#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 23:23
FileName: P3726. 移除十进制表示中的所有零.py
Description:
"""


class Solution:
    def removeZeros(self, n: int) -> int:
        return int(''.join(digit for digit in str(n) if digit != '0'))


if __name__ == '__main__':
    solution = Solution().removeZeros(1020030)
    print(solution)

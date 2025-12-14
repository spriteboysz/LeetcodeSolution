#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 22:59
FileName: P3726. 移除十进制表示中的所有零.py
Description:
"""


class Solution:
    def removeZeros(self, n: int) -> int:
        return int(''.join(el for el in str(n) if el != '0'))


if __name__ == '__main__':
    s = Solution().removeZeros(n=1020030)
    print(s)

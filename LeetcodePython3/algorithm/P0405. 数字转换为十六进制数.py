#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 11:11
FileName: P0405. 数字转换为十六进制数.py
Description:
"""
from string import hexdigits


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num += 4294967296
        ss = []
        while num >= 16:
            num, mod = divmod(num, 16)
            ss.append(hexdigits[mod])
        ss.append(hexdigits[num])
        return ''.join(ss)[::-1]


if __name__ == '__main__':
    solution = Solution().toHex(num=15)
    print(solution)

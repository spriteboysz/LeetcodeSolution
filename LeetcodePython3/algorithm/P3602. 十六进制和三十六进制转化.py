#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 11:21
FileName: P3602. 十六进制和三十六进制转化.py
Description:
"""
from string import digits, ascii_uppercase


class Solution:

    @classmethod
    def calc(cls, num, base):
        s = digits + ascii_uppercase
        ss = []
        while num >= base:
            num, mod = divmod(num, base)
            ss.append(s[mod])
        ss.append(s[num])
        return ''.join(ss)[::-1]

    def concatHex36(self, n: int) -> str:
        return self.calc(n ** 2, 16) + self.calc(n ** 3, 36)


if __name__ == '__main__':
    solution = Solution().concatHex36(13)
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:39
FileName: P1844. 将所有数字用字符替换.py
Description:
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        ss = list(s)
        for i in range(len(ss)):
            if i % 2 == 0:
                continue
            ss[i] = chr(ord(ss[i - 1]) + int(ss[i]))
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().replaceDigits(s="a1b2c3d4e")
    print(solution)

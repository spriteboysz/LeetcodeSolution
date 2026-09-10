#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 14:23
FileName: LC/LCR 192. 把字符串转换成整数 (atoi).py
Description: 
"""
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        matches = re.findall(r'(^[-+]?\d+)', s.strip())
        if not matches:
            return 0
        num = int(matches[0])
        if num < -2 ** 31:
            return -2 ** 31
        if num >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        return num


if __name__ == '__main__':
    solution = Solution().myAtoi("words and 987")
    print('<None>' if not solution else f'{solution=}')

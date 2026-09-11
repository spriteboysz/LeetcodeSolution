#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 09:29
FileName: algorithm/P0008. 字符串转换整数 (atoi).py
Description: 
"""
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'([+-]?)(\d+)', s.strip())
        if not match:
            return 0

        flag, number = match.groups()
        flag = -1 if flag == '-' else 1

        num = 0
        for c in number:
            num = num * 10 + ord(c) - ord('0')
        return min(max(-2 ** 31, num * flag), 2 ** 31 - 1)


if __name__ == '__main__':
    solution = Solution().myAtoi(" -042")
    print('<None>' if solution is None else f'{solution=}')

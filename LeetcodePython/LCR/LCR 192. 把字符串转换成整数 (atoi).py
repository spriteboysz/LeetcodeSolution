#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-14 22:42
FileName: LCR/LCR 192. 把字符串转换成整数 (atoi).py
Description: 
"""
import re
from icecream import ic


class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'[+-]?\d+', s.strip())
        if not match:
            return 0
        num = int(match.group())
        if -2 ** 31 <= num <= 2 ** 31 - 1:
            return num
        return -2 ** 31 if num < -2 ** 31 else 2 ** 31 - 1


if __name__ == '__main__':
    solution = Solution().myAtoi("   -32")
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-14 22:57
FileName: algorithm/P0008. 字符串转换整数 (atoi).py
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
        if num < -2 ** 31:
            return -2 ** 31
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return num


if __name__ == '__main__':
    solution = Solution().myAtoi(s=" -042")
    ic(solution)

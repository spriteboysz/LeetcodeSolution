#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 11:31
FileName: P0504. 七进制数.py
Description:
"""
from string import digits


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        flag = '+' if num > 0 else '-'
        num = abs(num)
        ss = []
        while num >= 7:
            num, mod = divmod(num, 7)
            ss.append(digits[mod])
        ss.append(digits[num])
        return (flag + ''.join(ss)[::-1]).lstrip('+')


if __name__ == '__main__':
    solution = Solution().convertToBase7(-7)
    print(solution)

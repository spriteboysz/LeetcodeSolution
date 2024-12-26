#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-25 23:19
FileName: 面试题 05.02. 二进制数转字符串
Description:
"""


class Solution:
    def printBin(self, num: float) -> str:
        ss = '0.'
        while num and len(ss) < 32:
            num *= 2
            mod = int(num)
            num -= mod
            ss += str(mod)
        return 'ERROR' if num else ss


if __name__ == '__main__':
    solution = Solution().printBin(0.625)
    print(solution)

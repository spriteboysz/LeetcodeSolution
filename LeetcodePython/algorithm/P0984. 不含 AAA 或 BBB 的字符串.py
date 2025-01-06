#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-06 22:54
FileName: P0984. 不含 AAA 或 BBB 的字符串
Description:
"""

from icecream import ic


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ss = []
        while a > 0 and b > 0:
            if a > b:
                ss.append('aab')
                a -= 2
                b -= 1
            elif a < b:
                ss.append('bba')
                a -= 1
                b -= 2
            else:
                ss.append('ab')
                a -= 1
                b -= 1
        if a > 0:
            ss.append('a' * a)
        if b > 0:
            ss.append('b' * b)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().strWithout3a3b(4, 3)
    ic(solution)

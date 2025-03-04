#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-04 22:46
FileName: algorithm/P3461. 判断操作后字符串中的数字是否相等 I.py
Description: 
"""

from icecream import ic


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s = ''.join(str(sum(map(int, s[i - 1:i + 1])))[-1] for i in range(1, len(s)))
        return s[0] == s[1]


if __name__ == '__main__':
    solution = Solution().hasSameDigits(s="919")
    ic(solution)

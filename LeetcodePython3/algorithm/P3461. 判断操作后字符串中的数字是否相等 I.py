#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 23:04
FileName: P3461. 判断操作后字符串中的数字是否相等 I.py
Description:
"""
from itertools import pairwise


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s = ''.join(str((int(ch1) + int(ch2)) % 10) for ch1, ch2 in pairwise(s))
        return s[0] == s[1]


if __name__ == '__main__':
    solution = Solution().hasSameDigits(s="3902")
    print(solution)

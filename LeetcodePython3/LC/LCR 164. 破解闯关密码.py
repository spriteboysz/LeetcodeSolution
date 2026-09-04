#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 08:59
FileName: LC/LCR 164. 破解闯关密码.py
Description: 
"""
from functools import cmp_to_key

from typing import List


class Solution:
    def crackPassword(self, password: List[int]) -> str:
        def func(a, b):
            s1, s2 = str(a) + str(b), str(b) + str(a)
            if s1 == s2:
                return 0
            return 1 if s1 > s2 else -1

        return ''.join(map(str, sorted(password, key=cmp_to_key(func))))


if __name__ == '__main__':
    solution = Solution().crackPassword(password=[0, 3, 30, 34, 5, 9])
    print(solution)

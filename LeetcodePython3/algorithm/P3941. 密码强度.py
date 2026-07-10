#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-10 22:40
FileName: P3941. 密码强度.py
Description:
"""


class Solution:
    def passwordStrength(self, password: str) -> int:
        def calc(pw):
            if pw.isdecimal():
                return 3
            if pw.islower():
                return 1
            if pw.isupper():
                return 2
            return 5

        return sum(calc(el) for el in set(password))


if __name__ == '__main__':
    solution = Solution().passwordStrength(password="aA1!")
    print(solution)

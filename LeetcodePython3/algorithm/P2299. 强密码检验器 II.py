#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:32
FileName: P2299. 强密码检验器 II.py
Description:
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        flags = [False] * 4
        for i, ch in enumerate(password):
            if ch.islower():
                flags[0] = True
            if ch.isupper():
                flags[1] = True
            if ch.isdigit():
                flags[2] = True
            if ch in '!@#$%^&*()-+':
                flags[3] = True
            if i > 0 and password[i - 1] == ch:
                return False
        return all(flags)


if __name__ == '__main__':
    solution = Solution().strongPasswordCheckerII(password="IloveLe3tcode!")
    print(solution)

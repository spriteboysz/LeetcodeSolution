#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 20:44
FileName: P2299. 强密码检验器 II
Description:
"""

from string import ascii_lowercase, ascii_uppercase, digits

from icecream import ic


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        flags = [False] * 4
        for i, ch in enumerate(password):
            if ch in ascii_lowercase:
                flags[0] = True
            elif ch in ascii_uppercase:
                flags[1] = True
            elif ch in digits:
                flags[2] = True
            elif ch in "!@#$%^&*()-+":
                flags[3] = True
            if i > 0 and ch == password[i - 1]:
                return False
        return all(flags)


if __name__ == '__main__':
    solution = Solution().strongPasswordCheckerII(password="IloveLe3tcode!")
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-21 23:16
FileName: P0831. 隐藏个人信息.py
Description:
"""


class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.lower().split('@')
            return f'{name[0]}*****{name[-1]}@{domain}'
        else:
            digits = [digit for digit in s if digit.isdigit()]
            county, local = digits[:-10], digits[-10:]
            local = ''.join(local)
            local = f'***-***-{local[-4:]}'
            if county:
                return f'+{"*" * len(county)}-{local}'
            return local


if __name__ == '__main__':
    solution = Solution().maskPII("LeetCode@LeetCode.com")
    print(solution)
    solution = Solution().maskPII("1(234)567-890")
    print(solution)

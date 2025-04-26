#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 11:01
FileName: algorithm/P0831. 隐藏个人信息.py
Description: 
"""

from icecream import ic


class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            msg = f'{name[0]}*****{name[-1]}@{domain}'
        else:
            ss = [ch for ch in s if ch.isdigit()]
            msg = f"+{'*' * (len(ss) - 10)}-***-***-{''.join(ss[-4:])}".replace('+-', '')
        return msg


if __name__ == '__main__':
    solution = Solution().maskPII(s="LeetCode@LeetCode.com")
    ic(solution)
    solution = Solution().maskPII(s="1(234)567-890")
    ic(solution)

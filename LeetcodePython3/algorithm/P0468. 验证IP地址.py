#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 11:26
FileName: P0468. 验证IP地址.py
Description:
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            try:
                sections = queryIP.split('.')
                if len(sections) == 4 and all(0 <= int(num) < 256 for num in sections) and all(
                        not num.startswith('0') for num in sections if num != '0'):
                    return 'IPv4'
                return 'Neither'
            except ValueError:
                return 'Neither'
        elif ':' in queryIP:
            try:
                sections = queryIP.split(':')
                if len(sections) == 8 and all(len(num) <= 4 for num in sections) and all(int(num, 16) < 65536 for num in sections):
                    return 'IPv6'
                return 'Neither'
            except ValueError:
                return 'Neither'
        return 'Neither'


if __name__ == '__main__':
    solution = Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
    print(solution)

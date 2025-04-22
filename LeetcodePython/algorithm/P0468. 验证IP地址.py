#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 22:20
FileName: algorithm/P0468. 验证IP地址.py
Description: 
"""
from string import hexdigits
from icecream import ic


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            nums = queryIP.split('.')
            if len(nums) == 4 and all(num.isdigit() and 0 <= int(num) <= 255 and str(int(num)) == num for num in nums):
                return 'IPv4'
            return 'Neither'
        if ':' in queryIP:
            nums = queryIP.split(':')
            if len(nums) == 8 and all(0 < len(num) <= 4 and all(ch in hexdigits for ch in num) for num in nums):
                return 'IPv6'
            return 'Neither'
        return 'Neither'


if __name__ == '__main__':
    solution = Solution().validIPAddress("172.016.254.1")
    ic(solution)
    solution = Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 15:00
FileName: algorithm/P4030. 判断 ASCII 值回文.py
Description: 
"""


class Solution:
    def isPalindromic(self, s: str) -> bool:
        ss = ''.join(bin(ord(c))[2:].zfill(8) for c in s)
        return ss == ss[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindromic('ff')
    print('<None>' if solution is None else f'{solution=}')

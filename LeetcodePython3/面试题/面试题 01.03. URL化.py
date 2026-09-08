#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 08:56
FileName: 面试题/面试题 01.03. URL化.py
Description: 
"""


class Solution:
    def replaceSpaces(self, s: str, length: int) -> str:
        return s[:length].replace(' ', '%20')


if __name__ == '__main__':
    solution = Solution().replaceSpaces("Mr John Smith    ", 13)
    print('<None>' if not solution else f'{solution=}')

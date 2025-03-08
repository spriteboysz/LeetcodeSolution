#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-08 22:29
FileName: LCR/P1869. 哪种连续子字符串更长.py
Description: 
"""

from icecream import ic


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return max(len(el) for el in s.split('0')) > max(len(el) for el in s.split('1'))


if __name__ == '__main__':
    solution = Solution().checkZeroOnes(s="110100010")
    ic(solution)

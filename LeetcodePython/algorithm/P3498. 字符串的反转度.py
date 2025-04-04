#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 9:22
FileName: LCR/P3498. 字符串的反转度.py
Description: 
"""

from icecream import ic


class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - ord(ch) + ord('a')) * (i + 1) for i, ch in enumerate(s))


if __name__ == '__main__':
    solution = Solution().reverseDegree('abc')
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-25 22:59
FileName: algorithm/P2609. 最长平衡子字符串.py
Description: 
"""

from icecream import ic


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        for i in range(25, 0, -1):
            if ('0' * i + '1' * i) in s:
                return i * 2
        return 0


if __name__ == '__main__':
    solution = Solution().findTheLongestBalancedSubstring(s="01000111")
    ic(solution)

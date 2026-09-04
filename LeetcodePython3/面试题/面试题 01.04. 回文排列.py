#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 14:35
FileName: 面试题/面试题 01.04. 回文排列.py
Description: 
"""
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        return sum(cnt % 2 == 1 for cnt in counter.values()) <= 1


if __name__ == '__main__':
    solution = Solution().canPermutePalindrome('tactcoa')
    print(solution)

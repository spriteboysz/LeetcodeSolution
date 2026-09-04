#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 21:09
FileName: LC/LCR 032. 有效的字母异位词.py
Description: 
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s != t and Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution().isAnagram(s="anagram", t="nagaram")
    print(solution)

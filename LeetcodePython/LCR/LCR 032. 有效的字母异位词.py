#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 13:39
FileName: LCR 032. 有效的字母异位词
Description:
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t or len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution().isAnagram(s="anagram", t="nagaram")
    print(solution)

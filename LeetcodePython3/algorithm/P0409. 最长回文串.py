#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 20:06
FileName: P0409. 最长回文串.py
Description:
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans, odd = 0, 0
        for cnt in counter.values():
            if cnt % 2 == 1:
                odd = 1
            ans += (cnt // 2) * 2
        return ans + odd


if __name__ == '__main__':
    solution = Solution().longestPalindrome(s="abccccdd")
    print(solution)

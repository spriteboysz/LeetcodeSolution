#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-13 23:16
FileName: interview/P3517. 最小回文排列 I.py
Description: 
"""

from icecream import ic


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        alphabet = [0] * 26
        for ch in s:
            alphabet[ord(ch) - ord('a')] += 1
        ss, mid = '', ''
        for i, num in enumerate(alphabet):
            if num == 0:
                continue
            ss += chr(ord('a') + i) * (num // 2)
            if num % 2 == 1:
                mid = chr(ord('a') + i)
        return ss + mid + ss[::-1]


if __name__ == '__main__':
    solution = Solution().smallestPalindrome(s="daccad")
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 10:42
FileName: algorithm/P0647. 回文子串.py
Description: 
"""

from icecream import ic


class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(s[j:i] and s[j:i] == s[j:i][::-1] for i in range(len(s) + 1) for j in range(i))


if __name__ == '__main__':
    solution = Solution().countSubstrings('abc')
    ic(solution)

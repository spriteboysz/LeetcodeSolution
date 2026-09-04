#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 21:07
FileName: LC/LCR 020. 回文子串.py
Description: 
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s) + 1):
            for j in range(i):
                if s[j:i] and s[j:i] == s[j:i][::-1]:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countSubstrings('ss')
    print(solution)

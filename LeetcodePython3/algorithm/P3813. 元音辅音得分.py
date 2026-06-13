#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 09:03
FileName: P3813. 元音辅音得分.py
Description:
"""


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v, c = 0, 0
        for ch in s:
            if not ch.isalpha():
                continue
            if ch in 'aeiou':
                v += 1
            else:
                c += 1
        return 0 if c == 0 else v // c


if __name__ == '__main__':
    solution = Solution().vowelConsonantScore(s="cooear")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 21:58
FileName: P1876. 长度为三且各字符不同的子字符串.py
Description:
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(len(s[i - 3:i]) == len(set(s[i - 3:i])) for i in range(3, len(s) + 1))


if __name__ == '__main__':
    solution = Solution().countGoodSubstrings(s="xyzzaz")
    print(solution)

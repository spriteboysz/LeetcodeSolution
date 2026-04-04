#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-04 21:07
FileName: P3884. 双端字符匹配.py
Description:
"""


class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for i, ch in enumerate(s):
            if ch == s[- i - 1]:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().firstMatchingIndex(s="abcacbd")
    print(solution)

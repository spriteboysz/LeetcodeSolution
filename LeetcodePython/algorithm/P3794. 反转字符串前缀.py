#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-01-17 10:05
FileName: P3794. 反转字符串前缀.py
Description:
"""


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]


if __name__ == '__main__':
    solution = Solution().reversePrefix('abcd', 2)
    print(solution)

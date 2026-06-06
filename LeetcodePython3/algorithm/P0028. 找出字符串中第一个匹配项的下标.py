#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 13:47
FileName: P0028. 找出字符串中第一个匹配项的下标.py
Description:
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)


if __name__ == '__main__':
    solution = Solution().strStr(haystack = "sadbutsad", needle = "sad")
    print(solution)

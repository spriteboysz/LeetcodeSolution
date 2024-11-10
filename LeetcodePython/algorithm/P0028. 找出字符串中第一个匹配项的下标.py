#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 17:02
FileName: P0028. 找出字符串中第一个匹配项的下标
Description:
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().strStr(haystack="sad", needle="sad")
    print(solution)

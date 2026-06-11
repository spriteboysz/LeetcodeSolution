#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 22:31
FileName: P3083. 字符串及其反转中是否存在同一子字符串.py
Description:
"""


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        return any(s[i: i + 2][::-1] in s for i in range(len(s) - 1))


if __name__ == '__main__':
    solution = Solution().isSubstringPresent(s="leetcode")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-17 23:04
FileName: P0459. 重复的子字符串
Description:
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


if __name__ == '__main__':
    solution = Solution().repeatedSubstringPattern(s="abcabcabcabc")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 14:22
FileName: 面试题/面试题 01.01. 判定字符是否唯一.py
Description: 
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        ss = list(astr)
        return len(ss) == len(set(ss))


if __name__ == '__main__':
    solution = Solution().isUnique('abc')
    print(solution)

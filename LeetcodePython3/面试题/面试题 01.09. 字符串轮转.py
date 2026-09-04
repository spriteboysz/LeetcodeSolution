#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 11:22
FileName: 面试题/面试题 01.09. 字符串轮转.py
Description: 
"""


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in (s1 + s1)


if __name__ == '__main__':
    solution = Solution().isFlipedString(s1="waterbottle", s2="erbottlewat")
    print(solution)

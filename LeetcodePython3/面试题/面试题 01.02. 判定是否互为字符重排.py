#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 14:38
FileName: 面试题/面试题 01.02. 判定是否互为字符重排.py
Description: 
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    solution = Solution().CheckPermutation(s1="abc", s2="bca")
    print(solution)

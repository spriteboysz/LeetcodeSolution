#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 23:09
FileName: P2839. 判断通过操作能否让字符串相等 I
Description:
"""

from icecream import ic


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])


if __name__ == '__main__':
    solution = Solution().canBeEqual(s1="abcd", s2="cdab")
    ic(solution)

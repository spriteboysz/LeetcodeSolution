#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:25
FileName: P2351. 第一个出现两次的字母.py
Description:
"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().repeatedCharacter(s="abccbaacz")
    print(solution)

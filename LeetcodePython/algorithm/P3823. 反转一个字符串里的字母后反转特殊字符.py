#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-02-28 22:49
FileName: P3823. 反转一个字符串里的字母后反转特殊字符.py
Description:
"""


class Solution:
    def reverseByType(self, s: str) -> str:
        lower = [ch for ch in s if ch.islower()]
        other = [ch for ch in s if not ch.islower()]
        return ''.join(lower.pop() if ch.islower() else other.pop() for ch in s)


if __name__ == '__main__':
    solution = Solution().reverseByType(")ebc#da@f(")
    print(solution)

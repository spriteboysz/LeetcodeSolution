#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:50
FileName: P3823. 反转一个字符串里的字母后反转特殊字符.py
Description:
"""


class Solution:
    def reverseByType(self, s: str) -> str:
        ss, ss1, ss2 = [], [], []
        for ch in s:
            if ch.islower():
                ss1.append(ch)
            else:
                ss2.append(ch)
        for ch in s:
            if ch.islower():
                ss.append(ss1.pop())
            else:
                ss.append(ss2.pop())
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().reverseByType(s=")ebc#da@f(")
    print(solution)

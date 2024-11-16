#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 14:06
FileName: P1417. 重新格式化字符串
Description:
"""


class Solution:
    def reformat(self, s: str) -> str:
        s1, s2 = [], []
        for ch in s:
            if ch.isdigit():
                s1.append(ch)
            else:
                s2.append(ch)
        if abs(len(s1) - len(s2)) >= 2:
            return ''
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        ss = [''] * len(s)
        ss[::2], ss[1::2] = s1, s2
        return ''.join(ss)

if __name__ == '__main__':
    solution = Solution().reformat(s="covid2019")
    print(solution)

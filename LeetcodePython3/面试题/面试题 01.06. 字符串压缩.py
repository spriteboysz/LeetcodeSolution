#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 16:25
FileName: 面试题/面试题 01.06. 字符串压缩.py
Description: 
"""


class Solution:
    def compressString(self, s: str) -> str:
        if s == '':
            return ''
        ss, count = [], []
        curr, cnt = s[0], 1
        for c in s:
            if not ss or c != curr:
                ss.append(curr)
                count.append(cnt)
                cnt = 1
                curr = c
            else:
                cnt += 1
        ss.append(curr)
        count.append(cnt)
        s1 = ''.join(f'{c}{cnt}' for c, cnt in zip(ss[1:], count[1:]))
        return s1 if len(s1) < len(s) else s


if __name__ == '__main__':
    solution = Solution().compressString("aabcccccaaa")
    print('<None>' if not solution else f'{solution=}')

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:50
FileName: P2810. 故障键盘.py
Description:
"""


class Solution:
    def finalString(self, s: str) -> str:
        ss = []
        for ch in s:
            if ch == 'i':
                ss.reverse()
            else:
                ss.append(ch)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().finalString(s="string")
    print(solution)

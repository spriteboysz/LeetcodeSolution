#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 22:43
FileName: P1417. 重新格式化字符串.py
Description:
"""


class Solution:
    def reformat(self, s: str) -> str:
        ss1 = [ch for ch in s if ch.isdigit()]
        ss2 = [ch for ch in s if ch.isalpha()]
        if abs(len(ss1) - len(ss2)) > 1:
            return ''
        ans = [''] * len(s)
        ans[::2], ans[1::2] = sorted([ss1, ss2], key=len, reverse=True)
        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution().reformat(s="covid2019")
    print(solution)

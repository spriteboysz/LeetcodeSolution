#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 21:30
FileName: P3019. 按键变更的次数.py
Description:
"""


class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt, cur = 0, s[0].lower()
        for ch in s.lower():
            if ch != cur:
                cur = ch
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countKeyChanges(s="aAbBcC")
    print(solution)

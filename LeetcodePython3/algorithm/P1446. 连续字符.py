#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:06
FileName: P1446. 连续字符.py
Description:
"""


class Solution:
    def maxPower(self, s: str) -> int:
        maximum, curr = 1, 1
        for i, ch in enumerate(s[1:], start=1):
            if ch == s[i - 1]:
                curr += 1
                maximum = max(maximum, curr)
            else:
                curr = 1
        return maximum


if __name__ == '__main__':
    solution = Solution().maxPower('leetcodeee')
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 22:36
FileName: P3168. 候诊室中的最少椅子数.py
Description:
"""


class Solution:
    def minimumChairs(self, s: str) -> int:
        curr, maximum = 0, 0
        for ch in s:
            if ch == 'E':
                curr += 1
            else:
                curr -= 1
            maximum = max(maximum, curr)
        return maximum


if __name__ == '__main__':
    solution = Solution().minimumChairs(s="ELELEEL")
    print(solution)

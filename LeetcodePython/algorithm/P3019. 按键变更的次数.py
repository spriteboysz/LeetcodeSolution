#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 22:31
FileName: P3019. 按键变更的次数
Description:
"""

from icecream import ic


class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum(s[i - 1] != s[i] for i in range(1, len(s)))


if __name__ == '__main__':
    solution = Solution().countKeyChanges(s="aAbBcC")
    ic(solution)

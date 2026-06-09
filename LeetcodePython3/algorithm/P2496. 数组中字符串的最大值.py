#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 23:10
FileName: P2496. 数组中字符串的最大值.py
Description:
"""
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(s) if all(ch.isdigit() for ch in s) else len(s) for s in strs)


if __name__ == '__main__':
    solution = Solution().maximumValue(strs=["alic3", "bob", "3", "4", "00000"])
    print(solution)

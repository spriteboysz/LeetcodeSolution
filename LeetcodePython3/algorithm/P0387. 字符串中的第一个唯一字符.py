#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:56
FileName: P0387. 字符串中的第一个唯一字符.py
Description:
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, ch in enumerate(s):
            if counter.get(ch, 0) == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().firstUniqChar(s="leetcode")
    print(solution)

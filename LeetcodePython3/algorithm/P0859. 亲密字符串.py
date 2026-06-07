#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 11:14
FileName: P0859. 亲密字符串.py
Description:
"""
from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            return len(set(list(s))) < len(s)
        if Counter(s) != Counter(goal):
            return False
        return sum(ch1 != ch2 for ch1, ch2 in zip(s, goal)) == 2


if __name__ == '__main__':
    solution = Solution().buddyStrings(s="ab", goal="ba")
    print(solution)

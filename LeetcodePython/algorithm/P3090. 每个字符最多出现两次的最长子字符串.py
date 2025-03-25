#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-25 23:14
FileName: algorithm/P3090. 每个字符最多出现两次的最长子字符串.py
Description: 
"""
from collections import defaultdict
from icecream import ic


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maximum, pos = 0, 0
        dic = defaultdict(int)
        for i, ch in enumerate(s):
            dic[ch] += 1
            while dic[ch] > 2:
                dic[s[pos]] -= 1
                pos += 1
            maximum = max(maximum, i - pos + 1)
        return maximum


if __name__ == '__main__':
    solution = Solution().maximumLengthSubstring(s="bcbbbcba")
    ic(solution)

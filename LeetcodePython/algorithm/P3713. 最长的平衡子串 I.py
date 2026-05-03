#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-26 21:05
FileName: P3713. 最长的平衡子串 I.py
Description:
"""
from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)):
            dic = defaultdict(int)
            for j in range(i, len(s)):
                dic[s[j]] += 1
                if len(set(dic.values())) == 1:
                    maximum = max(maximum, j - i + 1)
        return maximum


if __name__ == '__main__':
    solution = Solution().longestBalanced(s="a")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-20 23:01
FileName: P3438. 找到字符串中合法的相邻数字
Description:
"""

from collections import defaultdict

from icecream import ic


class Solution:
    def findValidPair(self, s: str) -> str:
        dic = defaultdict(int)
        for ch in s:
            dic[ch] += 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i] and int(s[i - 1]) == dic[s[i - 1]] and int(s[i]) == dic[s[i]]:
                return s[i - 1:i + 1]
        return ''


if __name__ == '__main__':
    solution = Solution().findValidPair(s="2523533")
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-05 19:05
FileName: 面试题/LCR 014. 字符串的排列.py
Description: 
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        counter1, counter2 = Counter(s1), Counter(s2[:m])
        if counter1 == counter2:
            return True
        for i in range(m, n):
            counter2[s2[i - m]] -= 1
            counter2[s2[i]] += 1
            if counter1 == counter2:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().checkInclusion(s1="ab", s2="eidbaooo")
    print(solution)

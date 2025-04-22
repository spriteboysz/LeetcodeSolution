#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 22:39
FileName: algorithm/P0567. 字符串的排列.py
Description: 
"""
from collections import Counter
from icecream import ic


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        m, n = len(s1), len(s2)
        counter2 = Counter(s2[:m])
        if counter1 == counter2:
            return True
        for i in range(1, n - m + 1):
            counter2[s2[i - 1]] -= 1
            counter2[s2[i + m - 1]] += 1
            if counter1 == counter2:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().checkInclusion(s1="ab", s2="eidboooab")
    ic(solution)

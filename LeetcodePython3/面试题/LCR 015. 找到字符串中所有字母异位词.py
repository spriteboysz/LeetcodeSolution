#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-05 19:12
FileName: 面试题/LCR 015. 找到字符串中所有字母异位词.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        anagrams = []
        counter1, counter2 = Counter(p), Counter(s[:m])
        if counter1 == counter2:
            anagrams.append(0)
        for i in range(m, n):
            counter2[s[i - m]] -= 1
            counter2[s[i]] += 1
            if counter1 == counter2:
                anagrams.append(i - m + 1)
        return anagrams


if __name__ == '__main__':
    solution = Solution().findAnagrams(s="abab", p="ab")
    print(solution)

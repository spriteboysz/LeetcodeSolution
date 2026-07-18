#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 11:00
FileName: P0438. 找到字符串中所有字母异位词.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s += '#'
        n, m = len(s), len(p)
        if n - 1 < m:
            return []

        counter1, counter2 = Counter(p), Counter(s[:m])
        anagrams = []
        for i in range(n - m):
            if counter1 == counter2:
                anagrams.append(i)
            counter2[s[i]] -= 1
            counter2[s[i + m]] += 1
        return anagrams


if __name__ == '__main__':
    solution = Solution().findAnagrams(s="abab", p="ab")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-09 23:14
FileName: P0438. 找到字符串中所有字母异位词
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        counter1, counter2 = Counter(p), Counter(s[:n])
        index = []
        if counter1 == counter2:
            index.append(0)
        for i in range(n, len(s)):
            counter2[s[i - n]] -= 1
            counter2[s[i]] += 1
            if counter1 == counter2:
                index.append(i - n + 1)
        return index


if __name__ == '__main__':
    solution = Solution().findAnagrams(s="abab", p="ab")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-02 23:10
FileName: LCR 015. 找到字符串中所有字母异位词
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        counter, counter1 = Counter(p), Counter(s[:m])
        anagrams = []
        for i in range(n):
            if counter == counter1:
                anagrams.append(i)
            if i + m >= n:
                break
            counter1[s[i]] -= 1
            counter1[s[i + m]] += 1
        return anagrams


if __name__ == '__main__':
    solution = Solution().findAnagrams(s="cbaebabacdcba", p="abc")
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 11:50
FileName: P2506. 统计相似字符串对的数目.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [''.join(sorted(set(word))) for word in words]
        return sum(v * (v - 1) // 2 for v in Counter(words).values())


if __name__ == '__main__':
    solution = Solution().similarPairs(words=["aba", "aabb", "abcd", "bac", "aabc"])
    print(solution)

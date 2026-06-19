#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 11:34
FileName: P2255. 统计是给定字符串前缀的字符串数目.py
Description:
"""
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(word) for word in words)

if __name__ == '__main__':
    solution = Solution().countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc")
    print(solution)

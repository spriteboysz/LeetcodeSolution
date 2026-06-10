#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:39
FileName: P2185. 统计包含给定前缀的字符串.py
Description:
"""
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)


if __name__ == '__main__':
    solution = Solution().prefixCount(words=["pay", "attention", "practice", "attend"], pref="at")
    print(solution)

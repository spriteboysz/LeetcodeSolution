#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 22:40
FileName: P2255. 统计是给定字符串前缀的字符串数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(word) for word in words)


if __name__ == '__main__':
    solution = Solution().countPrefixes(words=["a", "b", "c", "ab", "bc", "abc"], s="abc")
    ic(solution)

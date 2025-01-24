#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 22:30
FileName: P2185. 统计包含给定前缀的字符串
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([word.startswith(pref) for word in words])


if __name__ == '__main__':
    solution = Solution().prefixCount(words=["pay", "attention", "practice", "attend"], pref="at")
    ic(solution)

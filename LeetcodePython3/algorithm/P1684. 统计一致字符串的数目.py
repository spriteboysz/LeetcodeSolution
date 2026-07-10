#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 23:28
FileName: P1684. 统计一致字符串的数目.py
Description:
"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = set(allowed)
        return sum(set(word) - seen == set() for word in words)


if __name__ == '__main__':
    solution = Solution().countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"])
    print(solution)

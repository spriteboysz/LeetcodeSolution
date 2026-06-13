#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:37
FileName: P1941. 检查是否所有字符出现次数相同.py
Description:
"""
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1


if __name__ == '__main__':
    solution = Solution().areOccurrencesEqual(s="abacbc")
    print(solution)

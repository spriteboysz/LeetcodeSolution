#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 23:12
FileName: P1941. 检查是否所有字符出现次数相同
Description:
"""
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        return len(set(counter.values())) == 1


if __name__ == '__main__':
    solution = Solution().areOccurrencesEqual(s="abacbc")
    print(solution)

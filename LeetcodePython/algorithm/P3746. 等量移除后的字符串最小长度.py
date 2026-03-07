#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-01 21:59
FileName: P3746. 等量移除后的字符串最小长度.py
Description:
"""

from collections import Counter


class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        count = Counter(s)
        return abs(count.get('a', 0) - count.get('b', 0))


if __name__ == '__main__':
    solution = Solution().minLengthAfterRemovals('aabbab')
    print(solution)

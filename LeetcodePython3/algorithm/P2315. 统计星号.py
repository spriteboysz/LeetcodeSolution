#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:20
FileName: P2315. 统计星号.py
Description:
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(segment.count('*') for i, segment in enumerate(s.split('|')) if i % 2 == 0)


if __name__ == '__main__':
    solution = Solution().countAsterisks(s="l|*e*et|c**o|*de|")
    print(solution)

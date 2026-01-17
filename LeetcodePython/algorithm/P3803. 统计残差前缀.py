#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-01-17 09:53
FileName: P3803. 统计残差前缀.py
Description:
"""


class Solution:
    def residuePrefixes(self, s: str) -> int:
        return sum(len(set(s[:i + 1])) == (i + 1) % 3 for i, ch in enumerate(s))


if __name__ == '__main__':
    solution = Solution().residuePrefixes('abc')
    print(solution)

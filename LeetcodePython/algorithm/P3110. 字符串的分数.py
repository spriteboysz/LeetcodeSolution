#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 20:33
FileName: P3110. 字符串的分数
Description:
"""

from icecream import ic


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s)))


if __name__ == '__main__':
    solution = Solution().scoreOfString('hello')
    ic(solution)

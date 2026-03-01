#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-01 21:56
FileName: P3760. 不同首字母的子字符串数目.py
Description:
"""


class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))


if __name__ == '__main__':
    solution = Solution().maxDistinct('abcd')
    print(solution)

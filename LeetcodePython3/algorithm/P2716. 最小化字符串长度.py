#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:15
FileName: P2716. 最小化字符串长度.py
Description:
"""


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


if __name__ == '__main__':
    solution = Solution().minimizedStringLength("baadccab")
    print(solution)

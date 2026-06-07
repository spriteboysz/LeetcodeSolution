#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:04
FileName: P0709. 转换成小写字母.py
Description:
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == '__main__':
    solution = Solution().toLowerCase(s="LOVELY")
    print(solution)

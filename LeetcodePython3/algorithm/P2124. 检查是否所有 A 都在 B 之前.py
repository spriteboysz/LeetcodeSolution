#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:00
FileName: P2124. 检查是否所有 A 都在 B 之前.py
Description:
"""


class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s


if __name__ == '__main__':
    solution = Solution().checkString(s="abab")
    print(solution)

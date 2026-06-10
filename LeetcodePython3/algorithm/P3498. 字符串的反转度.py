#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:20
FileName: P3498. 字符串的反转度.py
Description:
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i + 1) * (26 - ord(ch) + ord('a')) for i, ch in enumerate(s))


if __name__ == '__main__':
    solution = Solution().reverseDegree(s="zaza")
    print(solution)

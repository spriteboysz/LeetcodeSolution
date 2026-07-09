#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 23:07
FileName: P1689. 十-二进制数的最少数目.py
Description:
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(digit) for digit in n)


if __name__ == '__main__':
    solution = Solution().minPartitions(n="27346209830709182346")
    print(solution)

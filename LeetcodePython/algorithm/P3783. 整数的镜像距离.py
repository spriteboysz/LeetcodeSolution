#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-01-17 10:07
FileName: P3783. 整数的镜像距离.py
Description:
"""


class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))


if __name__ == '__main__':
    s = Solution().mirrorDistance(25)
    print(s)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 13:43
FileName: P0165. 比较版本号.py
Description:
"""
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def calc(version):
            return [int(v) for v in version.split('.')]

        for v1, v2 in zip_longest(calc(version1), calc(version2), fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


if __name__ == '__main__':
    solution = Solution().compareVersion('1.1', '1.10')
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 20:45
FileName: P0278. 第一个错误的版本.py
Description:
"""


def isBadVersion(version: int) -> bool:
    return version >= 3


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution().firstBadVersion(10)
    print(solution)

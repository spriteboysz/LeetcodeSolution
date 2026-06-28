#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 18:06
FileName: P2485. 找出中枢整数.py
Description:
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        total, acc = sum(range(1, n + 1)), 0
        for i in range(1, n + 1):
            acc += i
            if (acc - i) * 2 + i == total:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().pivotInteger(8)
    print(solution)

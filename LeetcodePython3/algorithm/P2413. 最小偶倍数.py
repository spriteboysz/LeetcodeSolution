#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:20
FileName: P2413. 最小偶倍数.py
Description:
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 2 if n % 2 == 1 else n


if __name__ == '__main__':
    solution = Solution().smallestEvenMultiple(5)
    print(solution)

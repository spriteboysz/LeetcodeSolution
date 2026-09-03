#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:15
FileName: algorithm/P1551. 使数组中所有元素相等的最小操作数.py
Description: 
"""


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return n * n // 4
        return (n + 1) * (n // 2) // 2


if __name__ == '__main__':
    solution = Solution().minOperations(6)
    print(solution)

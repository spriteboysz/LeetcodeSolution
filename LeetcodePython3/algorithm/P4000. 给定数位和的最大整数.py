#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-29 21:14
FileName: P4000. 给定数位和的最大整数.py
Description:
"""


class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if n * 9 < s:
            return -1
        ans = 10 ** (s // 9) - 1
        if s % 9:
            ans = ans * 10 + s % 9
            n -= 1
        return ans * 10 ** (n - s // 9)


if __name__ == '__main__':
    solution = Solution().largestInteger(2, 9)
    print(solution)

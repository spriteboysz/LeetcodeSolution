#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 19:14
FileName: P1486. 数组异或操作.py
Description:
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1, n):
            ans ^= start + 2 * i
        return ans


if __name__ == '__main__':
    solution = Solution().xorOperation(n=5, start=0)
    print(solution)

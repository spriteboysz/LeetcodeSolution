#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:42
FileName: P1486. 数组异或操作
Description:
"""

from icecream import ic


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            xor ^= start + 2 * i
        return xor


if __name__ == '__main__':
    solution = Solution().xorOperation(n=5, start=0)
    ic(solution)

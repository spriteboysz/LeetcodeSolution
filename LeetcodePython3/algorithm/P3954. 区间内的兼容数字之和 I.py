#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:37
FileName: P3954. 区间内的兼容数字之和 I.py
Description:
"""


class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(x for x in range(max(0, n - k), n + k + 1) if n & x == 0)


if __name__ == '__main__':
    solution = Solution().sumOfGoodIntegers(1, 13)
    print(solution)

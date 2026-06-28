#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 19:49
FileName: P3536. 两个数字的最大乘积.py
Description:
"""


class Solution:
    def maxProduct(self, n: int) -> int:
        ss = sorted(str(n))
        return int(ss[-1]) * int(ss[-2])


if __name__ == '__main__':
    solution = Solution().maxProduct(31)
    print(solution)

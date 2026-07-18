#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:19
FileName: P0371. 两整数之和.py
Description:
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum((a, b))


if __name__ == '__main__':
    solution = Solution().getSum(1, 2)
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 21:50
FileName: P3345. 最小可整除数位乘积 I
Description:
"""
from functools import reduce


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 1000):
            if reduce(lambda a, b: a * b, map(int, str(i))) % t == 0:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().smallestNumber(15, 3)
    print(solution)

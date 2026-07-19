#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 16:32
FileName: P0633. 平方数之和.py
Description:
"""
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, math.ceil(c ** 0.5)
        while a <= b:
            ss = a ** 2 + b ** 2
            if ss == c:
                return True
            if ss < c:
                a += 1
            else:
                b -= 1
        return False


if __name__ == '__main__':
    solution = Solution().judgeSquareSum(5)
    print(solution)

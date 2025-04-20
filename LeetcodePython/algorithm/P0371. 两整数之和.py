#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 20:56
FileName: algorithm/P0371. 两整数之和.py
Description: 
"""

from icecream import ic


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])


if __name__ == '__main__':
    solution = Solution().getSum(1, 2)
    ic(solution)

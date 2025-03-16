#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 11:28
FileName: algorithm/P0598. 区间加法 II.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min1, min2 = ops[0]
        for x, y in ops:
            min1 = min(min1, x)
            min2 = min(min2, y)
        return min1 * min2


if __name__ == '__main__':
    solution = Solution().maxCount(
        m=3, n=3,
        ops=[[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]])
    ic(solution)

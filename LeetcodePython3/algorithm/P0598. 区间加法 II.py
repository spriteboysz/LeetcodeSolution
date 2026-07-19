#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 09:32
FileName: P0598. 区间加法 II.py
Description:
"""
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_c = min((op[0] for op in ops), default=n)
        min_r = min((op[1] for op in ops), default=m)
        return min_c * min_r


if __name__ == '__main__':
    solution = Solution().maxCount(
        m=3, n=3,
        ops=[[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]])
    print(solution)

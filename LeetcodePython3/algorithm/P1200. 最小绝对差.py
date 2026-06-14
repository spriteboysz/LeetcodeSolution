#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:17
FileName: P1200. 最小绝对差.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = min(abs(a - b) for a, b in pairwise(arr))
        return [[a, b] for a, b in pairwise(arr) if abs(a - b) == minimum]


if __name__ == '__main__':
    solution = Solution().minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27])
    print(solution)

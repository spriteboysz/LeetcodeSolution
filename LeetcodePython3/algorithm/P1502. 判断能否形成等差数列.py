#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 19:04
FileName: P1502. 判断能否形成等差数列.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        return len({b - a for a, b in pairwise(sorted(arr))}) == 1


if __name__ == '__main__':
    solution = Solution().canMakeArithmeticProgression([3, 5, 1])
    print(solution)

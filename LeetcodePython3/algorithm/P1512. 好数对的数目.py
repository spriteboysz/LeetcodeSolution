#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 19:10
FileName: P1512. 好数对的数目.py
Description:
"""
from collections import Counter
from functools import lru_cache
from math import factorial
from typing import List


class Solution:
    @classmethod
    @lru_cache
    def calc(cls, n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(self.calc(v, 2) for v in Counter(nums).values() if v > 1)


if __name__ == '__main__':
    solution = Solution().numIdenticalPairs(nums=[1, 1, 1, 1])
    print(solution)

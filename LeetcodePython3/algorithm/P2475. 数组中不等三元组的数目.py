#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:24
FileName: P2475. 数组中不等三元组的数目.py
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        values = list(Counter(nums).values())
        cnt = 0
        for i, v1 in enumerate(values):
            for j, v2 in enumerate(values[:i]):
                for k, v3 in enumerate(values[:j]):
                    cnt += v1 * v2 * v3
        return cnt


if __name__ == '__main__':
    solution = Solution().unequalTriplets(nums=[4, 4, 2, 4, 3])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 15:22
FileName: algorithm/P3852. 不同频率的最小数对.py
Description: 
"""
from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        keys = sorted(counter)
        for i, k2 in enumerate(keys):
            for k1 in keys[:i]:
                if counter.get(k1, 0) != counter.get(k2, 0):
                    return [k1, k2]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().minDistinctFreqPair([1, 1, 2, 2, 3, 4])
    print('<None>' if solution is None else f'{solution=}')

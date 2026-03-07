#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-07 14:42
FileName: P3852. 不同频率的最小数对.py
Description:
"""

from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        a = min(nums)
        for num in sorted(set(nums)):
            if counter.get(num) != counter.get(a):
                return [a, num]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution().minDistinctFreqPair(nums=[1, 1, 2, 2, 3, 4])
    print(s)

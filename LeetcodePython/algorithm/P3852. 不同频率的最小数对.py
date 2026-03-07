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
        seen = sorted(set(nums))
        for num in seen[1:]:
            if counter.get(num) != counter.get(seen[0]):
                return [seen[0], num]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution().minDistinctFreqPair(nums=[1, 1, 2, 2, 3, 4])
    print(s)

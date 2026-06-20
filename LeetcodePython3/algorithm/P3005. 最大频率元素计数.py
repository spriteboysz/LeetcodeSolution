#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 19:10
FileName: P3005. 最大频率元素计数.py
Description:
"""
from typing import List, Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maximum = max(v for v in counter.values())
        return sum(v for v in counter.values() if v == maximum)


if __name__ == '__main__':
    solution = Solution().maxFrequencyElements([1, 2, 3, 4, 5])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 21:24
FileName: P1636. 按照频率将数组升序排序.py
Description:
"""
from typing import List, Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda num: (counter.get(num), -num))


if __name__ == '__main__':
    solution = Solution().frequencySort(nums=[1, 1, 2, 2, 2, 3])
    print(solution)

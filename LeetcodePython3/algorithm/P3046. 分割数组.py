#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 18:39
FileName: P3046. 分割数组.py
Description:
"""
from typing import List, Counter


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return all(v <= 2 for v in counter.values())


if __name__ == '__main__':
    solution = Solution().isPossibleToSplit(nums=[1, 1, 2, 2, 3, 4])
    print(solution)

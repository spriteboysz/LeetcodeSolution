#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 22:10
FileName: P0229. 多数元素 II.py
Description:
"""
from typing import List, Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        return [k for k, v in counter.items() if v > n // 3]


if __name__ == '__main__':
    solution = Solution().majorityElement(nums=[3, 2, 3])
    print(solution)

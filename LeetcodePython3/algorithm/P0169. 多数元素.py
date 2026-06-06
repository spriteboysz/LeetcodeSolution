#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:16
FileName: P0169. 多数元素.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num, cnt in counter.items():
            if cnt > len(nums) // 2:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().majorityElement(nums=[2, 2, 1, 1, 1, 2, 2])
    print(solution)

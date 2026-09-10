#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 15:38
FileName: 面试题/面试题 17.10. 主要元素.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v > len(nums) / 2:
                return k
        return -1


if __name__ == '__main__':
    solution = Solution().majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5])
    print('<None>' if solution is None else f'{solution=}')

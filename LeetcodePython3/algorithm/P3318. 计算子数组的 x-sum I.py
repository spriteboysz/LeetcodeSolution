#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-11 15:31
FileName: LC/P3318. 计算子数组的 x-sum I.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def calc(nums2):
            counter = Counter(nums2)
            if len(counter) <= x:
                return sum(nums2)
            keys = sorted(counter, key=lambda el: (counter[el], el), reverse=True)[:x]
            return sum(counter[key] * key for key in keys)

        return [calc(nums[i:i + k]) for i in range(len(nums) - k + 1)]


if __name__ == '__main__':
    solution = Solution().findXSum(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2)
    print('<None>' if solution is None else f'{solution=}')

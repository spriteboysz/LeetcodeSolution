#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-12 23:08
FileName: algorithm/P3011. 判断一个数组是否可以变为有序.py
Description: 
"""
from itertools import pairwise
from typing import List

from icecream import ic


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        group, curr, k = [], [nums[0]], nums[0].bit_count()
        for i in range(1, len(nums)):
            if nums[i].bit_count() != k:
                group.append(curr.copy())
                curr.clear()
                k = nums[i].bit_count()
            curr.append(nums[i])
        group.append(curr)
        nums2 = sum([sorted(sub) for sub in group], [])
        return all(y >= x for x, y in pairwise(nums2))


if __name__ == '__main__':
    solution = Solution().canSortArray(nums=[8, 4, 2, 30, 15])
    ic(solution)

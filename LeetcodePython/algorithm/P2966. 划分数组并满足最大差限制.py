#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-13 17:49
FileName: algorithm/P2966. 划分数组并满足最大差限制.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] <= k:
                arr.append(nums[i:i + 3])
            else:
                return []
        return arr


if __name__ == '__main__':
    solution = Solution().divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2)
    ic(solution)

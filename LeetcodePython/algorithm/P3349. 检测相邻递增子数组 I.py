#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-26 21:57
FileName: algorithm/P3349. 检测相邻递增子数组 I.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 2 * k + 1):
            flag1 = all(nums[j] > nums[j - 1] for j in range(i + 1, i + k))
            flag2 = all(nums[j] > nums[j - 1] for j in range(i + 1 + k, i + k * 2))
            if flag1 and flag2:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().hasIncreasingSubarrays(nums=[19, 4, 19, 6, 18], k=2)
    ic(solution)

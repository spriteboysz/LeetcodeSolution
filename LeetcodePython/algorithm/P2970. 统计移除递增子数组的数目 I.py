#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 21:25
FileName: algorithm/P2970. 统计移除递增子数组的数目 I.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                nums2 = nums[:i] + nums[j:]
                if nums2 == sorted(set(nums2)):
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().incremovableSubarrayCount([1, 2, 3, 4, 5])
    ic(solution)

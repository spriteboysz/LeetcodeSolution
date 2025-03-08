#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-06 23:28
FileName: LCR/P2395. 和相等的子数组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] in seen:
                return True
            seen.add(nums[i] + nums[i - 1])
        return False


if __name__ == '__main__':
    solution = Solution().findSubarrays([4, 2, 4])
    ic(solution)

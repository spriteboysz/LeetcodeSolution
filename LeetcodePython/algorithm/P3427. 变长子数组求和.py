#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 21:34
FileName: P3427. 变长子数组求和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            total += sum(nums[start:i + 1])
        return total


if __name__ == '__main__':
    solution = Solution().subarraySum([2, 3, 1])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 20:01
FileName: P3392. 统计符合条件长度为 3 的子数组数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum((nums[i - 2] + nums[i]) * 2 == nums[i - 1] for i in range(2, len(nums)))


if __name__ == '__main__':
    solution = Solution().countSubarrays(nums=[1, 2, 1, 4, 1])
    ic(solution)

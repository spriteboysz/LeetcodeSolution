#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-29 21:04
FileName: P3423. 循环数组中相邻元素的最大差值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        return max(abs(nums[i] - nums[i - 1]) for i in range(1, len(nums)))


if __name__ == '__main__':
    solution = Solution().maxAdjacentDistance([1, 2, 4])
    ic(solution)

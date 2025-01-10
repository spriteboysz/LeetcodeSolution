#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 21:49
FileName: P2016. 增量元素之间的最大差值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimum, maximum = nums[0], -1
        for num in nums:
            if num > minimum:
                maximum = max(maximum, num - minimum)
            else:
                minimum = num
        return maximum


if __name__ == '__main__':
    solution = Solution().maximumDifference(nums=[7, 1, 5, 4])
    ic(solution)

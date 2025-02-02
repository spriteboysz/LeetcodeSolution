#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 22:41
FileName: P2717. 半有序排列
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        maximum, minimum = max(nums), min(nums)
        maximum, minimum = nums.index(maximum), nums.index(minimum)
        return minimum + len(nums) - 1 - maximum - int(minimum > maximum)


if __name__ == '__main__':
    solution = Solution().semiOrderedPermutation(nums=[2, 4, 1, 3])
    ic(solution)

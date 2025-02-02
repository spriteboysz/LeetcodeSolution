#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 11:32
FileName: P2460. 对数组执行操作
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        nums = [num for num in nums if num > 0]
        m = len(nums)
        nums.extend([0] * (n - m))
        return nums


if __name__ == '__main__':
    solution = Solution().applyOperations(nums=[1, 2, 2, 1, 1, 0])
    ic(solution)

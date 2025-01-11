#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 22:37
FileName: P1909. 删除一个元素使数组严格递增
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] >= nums[i]:
                    return False
            return True

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return check(nums[:i - 1] + nums[i:]) or check(nums[:i] + nums[i + 1:])
        return True


if __name__ == '__main__':
    solution = Solution().canBeIncreasing([105, 924, 32, 968])
    ic(solution)

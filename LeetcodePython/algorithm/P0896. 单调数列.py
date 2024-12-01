#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 19:59
FileName: P0896. 单调数列
Description:
"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums1 = [nums[i] >= nums[i - 1] for i in range(1, len(nums))]
        nums2 = [nums[i] <= nums[i - 1] for i in range(1, len(nums))]
        return all(nums1) or all(nums2)


if __name__ == '__main__':
    solution = Solution().isMonotonic(nums=[1, 2, 2, 3])
    print(solution)

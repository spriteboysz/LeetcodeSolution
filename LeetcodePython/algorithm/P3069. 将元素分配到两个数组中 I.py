#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 22:27
FileName: P3069. 将元素分配到两个数组中 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1, nums2 = [nums[0]], [nums[1]]
        for num in nums[2:]:
            if nums1[-1] > nums2[-1]:
                nums1.append(num)
            else:
                nums2.append(num)
        return nums1 + nums2


if __name__ == '__main__':
    solution = Solution().resultArray([5, 4, 3, 8])
    ic(solution)

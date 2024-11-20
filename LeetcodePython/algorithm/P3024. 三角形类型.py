#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-20 22:36
FileName: P3024. 三角形类型
Description:
"""
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return 'none'
        if len(set(nums)) == 1:
            return 'equilateral'
        if len(set(nums)) == 2:
            return 'isosceles'
        return 'scalene'


if __name__ == '__main__':
    solution = Solution().triangleType([3, 3, 3])
    print(solution)

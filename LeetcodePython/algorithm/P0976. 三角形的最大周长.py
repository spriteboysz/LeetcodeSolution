#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 17:06
FileName: P0976. 三角形的最大周长
Description:
"""
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            if nums[i - 2] < nums[i - 1] + nums[i]:
                return sum(nums[i - 2:i + 1])
        return 0


if __name__ == '__main__':
    solution = Solution().largestPerimeter(nums=[1, 2, 1, 10])
    print(solution)

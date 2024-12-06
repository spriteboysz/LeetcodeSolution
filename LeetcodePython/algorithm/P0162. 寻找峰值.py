#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 23:27
FileName: P0162. 寻找峰值
Description:
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i, num in enumerate(nums):
            if i == 0:
                if num > nums[1]:
                    return i
            if i == len(nums) - 1:
                if num > nums[-2]:
                    return i
            if nums[i - 1] < num and num > nums[i + 1]:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-06 23:16
FileName: P0080. 删除有序数组中的重复项 II.py
Description:
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                nums[i] = None
        nums[:] = [num for num in nums if num is not None]
        return len(nums)


if __name__ == '__main__':
    solution = Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
    print(solution)

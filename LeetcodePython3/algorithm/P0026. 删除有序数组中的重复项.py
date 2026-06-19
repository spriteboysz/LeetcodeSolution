#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 22:09
FileName: P0026. 删除有序数组中的重复项.py
Description:
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    solution = Solution().removeDuplicates([1, 1, 2])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 16:46
FileName: P0080. 删除有序数组中的重复项 II
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == '__main__':
    solution = Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
    ic(solution)

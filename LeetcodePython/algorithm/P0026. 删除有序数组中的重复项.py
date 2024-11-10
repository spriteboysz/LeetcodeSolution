#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 16:52
FileName: P0026. 删除有序数组中的重复项
Description:
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                k += 1
                nums[k - 1] = nums[i]
        return k


if __name__ == '__main__':
    solution = Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(solution)

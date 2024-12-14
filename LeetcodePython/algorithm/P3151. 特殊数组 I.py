#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-13 22:06
FileName: P3151. 特殊数组 I
Description:
"""
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = [num % 2 for num in nums]
        if nums[0] == nums[1]:
            return False
        for i, num in enumerate(nums[2:]):
            if i % 2 == 0:
                if num != nums[0]:
                    return False
            else:
                if num != nums[1]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution().isArraySpecial(nums=[2, 1])
    print(solution)

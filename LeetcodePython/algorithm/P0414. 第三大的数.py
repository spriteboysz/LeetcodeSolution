#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 23:35
FileName: P0414. 第三大的数
Description:
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse=True)
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]


if __name__ == '__main__':
    solution = Solution().thirdMax([2, 2, 3, 1])
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 20:14
FileName: P0414. 第三大的数.py
Description:
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) < 3:
            return max(nums)
        return nums[-3]


if __name__ == '__main__':
    solution = Solution().thirdMax([2, 2, 3, 1])
    print(solution)

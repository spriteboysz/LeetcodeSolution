#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-07 22:48
FileName: LCR/P2932. 找出强数对的最大异或值 I.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maximum = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[i:]:
                if abs(num1 - num2) <= min(num1, num2):
                    maximum = max(maximum, num1 ^ num2)
        return maximum


if __name__ == '__main__':
    solution = Solution().maximumStrongPairXor(nums=[1, 2, 3, 4, 5])
    ic(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 15:32
FileName: algorithm/P2932. 找出强数对的最大异或值 I.py
Description: 
"""
from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maximum = 0
        for num1 in nums:
            for num2 in nums:
                if abs(num1 - num2) <= min(num1, num2):
                    maximum = max(maximum, num1 ^ num2)
        return maximum


if __name__ == '__main__':
    solution = Solution().maximumStrongPairXor(nums=[1, 2, 3, 4, 5])
    print('<None>' if solution is None else f'{solution=}')

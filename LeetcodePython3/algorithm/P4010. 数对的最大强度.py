#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 15:27
FileName: algorithm/P4010. 数对的最大强度.py
Description: 
"""
import math


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        strengths = []
        for i, num1 in enumerate(nums):
            for num2 in nums[:i]:
                strengths.append(num1 * num2 // math.gcd(num1, num2) ** 2)
        return max(strengths)


if __name__ == '__main__':
    solution = Solution().maxPairStrength([4, 6, 8])
    print('<None>' if solution is None else f'{solution=}')

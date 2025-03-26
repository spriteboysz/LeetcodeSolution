#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-25 23:23
FileName: algorithm/P3411. 最长乘积等价子数组.py
Description: 
"""
from math import prod, gcd, lcm
from typing import List

from icecream import ic


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maximum, n = 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                curr = nums[i:j + 1]
                if prod(curr) == lcm(*curr) * gcd(*curr):
                    maximum = max(maximum, j - i + 1)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxLength(nums=[1, 2, 1, 2, 1, 1, 1])
    ic(solution)

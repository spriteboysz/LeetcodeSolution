#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 23:43
FileName: P2873. 有序三元组中的最大值 I.py
Description:
"""
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maximum = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:], start=i + 1):
                for k, c in enumerate(nums[j + 1:], start=j + 1):
                    maximum = max(maximum, (a - b) * c)
        return maximum


if __name__ == '__main__':
    solution = Solution().maximumTripletValue(nums=[1, 10, 3, 4, 19])
    print(solution)

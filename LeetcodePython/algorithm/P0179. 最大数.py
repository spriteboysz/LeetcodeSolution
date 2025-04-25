#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-24 23:39
FileName: algorithm/P0179. 最大数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[:i]):
                if num1 + num2 > num2 + num1:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int(''.join(nums)))


if __name__ == '__main__':
    solution = Solution().largestNumber(nums=[3, 30, 34, 5, 9])
    ic(solution)

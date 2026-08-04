#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 15:50
FileName: P3423. 循环数组中相邻元素的最大差值.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        return max(abs(num1 - num2) for num1, num2 in pairwise(nums))


if __name__ == '__main__':
    solution = Solution().maxAdjacentDistance([1, 2, 4])
    print(solution)

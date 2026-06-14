#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:25
FileName: P0896. 单调数列.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(num1 >= num2 for num1, num2 in pairwise(nums)) or all(num1 <= num2 for num1, num2 in pairwise(nums))


if __name__ == '__main__':
    solution = Solution().isMonotonic(nums=[1, 2, 2, 3])
    print(solution)

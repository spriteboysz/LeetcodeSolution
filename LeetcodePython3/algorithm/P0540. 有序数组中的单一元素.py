#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:27
FileName: P0540. 有序数组中的单一元素.py
Description:
"""
from typing import List
from functools import reduce


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda num1, num2: num1 ^ num2, nums)


if __name__ == '__main__':
    solution = Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(solution)

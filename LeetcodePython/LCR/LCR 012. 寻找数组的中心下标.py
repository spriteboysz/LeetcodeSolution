#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 10:55
FileName: LCR/LCR 012. 寻找数组的中心下标.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ss, acc = sum(nums), 0
        for i, num in enumerate(nums):
            if acc * 2 == ss - num:
                return i
            acc += num
        return -1


if __name__ == '__main__':
    solution = Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6])
    ic(solution)
